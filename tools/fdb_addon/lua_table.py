"""Parser minimo de tablas Lua, suficiente para los archivos Data/*.lua del addon ForeverDB.

Solo entiende datos: tablas `{...}`, claves `[expr]=` y `nombre=`, cadenas (comillas
simples, dobles y largas `[[...]]` / `[=[...]=]`), numeros (enteros, decimales,
hexadecimales, signo menos), `true`, `false` y `nil`. Nunca ejecuta codigo.

`parse_assignments(texto)` recorre el archivo y devuelve las asignaciones de nivel
superior `ns.a.b = <valor>` y `local x = <valor>`. Todo lo demas (bucles, funciones,
`local _, ns = ...`) se salta token a token.

Representacion en Python: una tabla sin claves explicitas es una `list`; si tiene
alguna clave explicita es un `dict` (las entradas posicionales llevan claves 1..n).
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Tuple

_TOKEN = re.compile(
    r"""
    (?P<ws>\s+)
  | (?P<comment>--(?:\[(?P<ceq>=*)\[[\s\S]*?\](?P=ceq)\]|[^\n]*))
  | (?P<longstr>\[(?P<leq>=*)\[[\s\S]*?\](?P=leq)\])
  | (?P<str>"(?:[^"\\\n]|\\[\s\S])*"|'(?:[^'\\\n]|\\[\s\S])*')
  | (?P<num>0[xX][0-9a-fA-F]+|(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)
  | (?P<name>[A-Za-z_][A-Za-z0-9_]*)
  | (?P<op>\.\.\.|\.\.|==|~=|<=|>=|[{}\[\]=,;.()+\-*/%#<>:^])
    """,
    re.VERBOSE,
)

_ESCAPES = {
    "n": "\n", "t": "\t", "r": "\r", "a": "\a", "b": "\b", "f": "\f", "v": "\v",
    "\\": "\\", '"': '"', "'": "'", "\n": "\n",
}


class LuaParseError(ValueError):
    pass


def _unescape(body: str) -> str:
    out: List[str] = []
    i, n = 0, len(body)
    while i < n:
        c = body[i]
        if c != "\\":
            out.append(c)
            i += 1
            continue
        i += 1
        if i >= n:
            break
        e = body[i]
        if e in _ESCAPES:
            out.append(_ESCAPES[e])
            i += 1
        elif e.isdigit():
            j = i
            while j < n and j - i < 3 and body[j].isdigit():
                j += 1
            out.append(chr(int(body[i:j])))
            i = j
        elif e == "x":
            out.append(chr(int(body[i + 1:i + 3], 16)))
            i += 3
        elif e == "z":
            i += 1
            while i < n and body[i].isspace():
                i += 1
        else:
            out.append(e)
            i += 1
    return "".join(out)


def tokenize(text: str) -> List[Tuple[str, Any]]:
    """Devuelve [(tipo, valor)] con tipo en str, num, name, op. Sin espacios ni comentarios."""
    toks: List[Tuple[str, Any]] = []
    pos, n = 0, len(text)
    match = _TOKEN.match
    while pos < n:
        m = match(text, pos)
        if not m:
            raise LuaParseError("caracter inesperado en %d: %r" % (pos, text[pos:pos + 20]))
        kind = m.lastgroup
        if kind in ("ceq", "leq"):  # grupos internos: buscar el principal
            kind = "comment" if m.group("comment") is not None else "longstr"
        val = m.group(0)
        pos = m.end()
        if kind in ("ws", "comment"):
            continue
        if kind == "longstr":
            eq = len(m.group("leq"))
            body = val[eq + 2:-(eq + 2)]
            if body.startswith("\r\n"):
                body = body[2:]
            elif body.startswith("\n"):
                body = body[1:]
            toks.append(("str", body))
        elif kind == "str":
            toks.append(("str", _unescape(val[1:-1])))
        elif kind == "num":
            if val[:2] in ("0x", "0X"):
                toks.append(("num", int(val, 16)))
            elif re.fullmatch(r"\d+", val):
                toks.append(("num", int(val)))
            else:
                toks.append(("num", float(val)))
        else:
            toks.append((kind, val))
    return toks


class _Parser:
    def __init__(self, toks: List[Tuple[str, Any]]):
        self.t = toks
        self.i = 0

    def peek(self, k: int = 0) -> Tuple[Optional[str], Any]:
        j = self.i + k
        return self.t[j] if j < len(self.t) else (None, None)

    def expect(self, kind: str, val: Any = None) -> Any:
        tk, tv = self.peek()
        if tk != kind or (val is not None and tv != val):
            raise LuaParseError("se esperaba %s %r, hay %s %r (token %d)" % (kind, val, tk, tv, self.i))
        self.i += 1
        return tv

    def value(self) -> Any:
        tk, tv = self.peek()
        if tk == "op" and tv == "{":
            return self.table()
        if tk == "op" and tv == "-":
            self.i += 1
            v = self.value()
            if not isinstance(v, (int, float)):
                raise LuaParseError("signo menos sobre un no numero")
            return -v
        if tk in ("str", "num"):
            self.i += 1
            # concatenacion de cadenas literales: "a" .. "b"
            if tk == "str":
                while self.peek() == ("op", ".."):
                    self.i += 1
                    nxt = self.value()
                    tv = tv + (nxt if isinstance(nxt, str) else str(nxt))
            return tv
        if tk == "name":
            self.i += 1
            if tv == "true":
                return True
            if tv == "false":
                return False
            if tv == "nil":
                return None
            # referencia a otra variable (ns.x): no es un dato, se descarta
            while self.peek() == ("op", ".") and self.peek(1)[0] == "name":
                self.i += 2
            return None
        raise LuaParseError("valor inesperado %s %r (token %d)" % (tk, tv, self.i))

    def table(self) -> Any:
        self.expect("op", "{")
        arr: List[Any] = []
        hashed: Dict[Any, Any] = {}
        while True:
            tk, tv = self.peek()
            if tk == "op" and tv == "}":
                self.i += 1
                break
            if tk == "op" and tv == "[":
                self.i += 1
                key = self.value()
                self.expect("op", "]")
                self.expect("op", "=")
                hashed[key] = self.value()
            elif tk == "name" and self.peek(1) == ("op", "="):
                self.i += 2
                hashed[tv] = self.value()
            else:
                arr.append(self.value())
            tk, tv = self.peek()
            if tk == "op" and tv in (",", ";"):
                self.i += 1
            elif not (tk == "op" and tv == "}"):
                raise LuaParseError("se esperaba , o } (token %d: %r)" % (self.i, tv))
        if not hashed:
            return arr
        for idx, v in enumerate(arr, 1):
            hashed.setdefault(idx, v)
        return hashed


def parse_value(text: str) -> Any:
    """Parsea una expresion Lua de datos; acepta un `return` inicial."""
    toks = tokenize(text)
    if toks and toks[0] == ("name", "return"):
        toks = toks[1:]
    p = _Parser(toks)
    v = p.value()
    return v


def parse_assignments(text: str) -> Dict[str, Any]:
    """Asignaciones de nivel superior: {'ns.qfQuests': {...}, 'local packed': {...}}."""
    toks = tokenize(text)
    p = _Parser(toks)
    out: Dict[str, Any] = {}
    n = len(toks)
    while p.i < n:
        tk, tv = p.peek()
        if tk == "name" and tv == "ns" and p.peek(1) == ("op", "."):
            j = p.i + 1
            path = ["ns"]
            while j + 1 < n and toks[j] == ("op", ".") and toks[j + 1][0] == "name":
                path.append(toks[j + 1][1])
                j += 2
            if j < n and toks[j] == ("op", "=") and (j + 1 >= n or toks[j + 1] != ("op", "=")):
                p.i = j + 1
                out[".".join(path)] = p.value()
                continue
            p.i = j
            continue
        if tk == "name" and tv == "local" and p.peek(1)[0] == "name" and p.peek(2) == ("op", "="):
            name = p.peek(1)[1]
            nxt = p.peek(3)
            if nxt[0] in ("str", "num") or nxt == ("op", "{"):
                p.i += 3
                out["local " + name] = p.value()
                continue
        p.i += 1
    return out


def parse_file(path) -> Dict[str, Any]:
    with open(path, encoding="utf-8") as fh:
        return parse_assignments(fh.read())
