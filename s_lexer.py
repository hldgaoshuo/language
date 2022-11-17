import io
import typing as t

from s_token import *
from utils import log


def spaces() -> t.List[str]:
    return [" ", "\n", "\r\n", "\r"]


def digits() -> t.List[str]:
    return ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def letters() -> t.List[str]:
    return [
        "a", "b", "c", "d", "e", "f", "g",
        "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q",
        "r", "s", "t",
        "u", "v", "w",
        "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q",
        "R", "S", "T",
        "U", "V", "W",
        "X", "Y", "Z",
    ]


def symbols() -> t.List[str]:
    return [
        "+", "-", "*", "/", "%",
        ",",
        ";",
        "{", "}",
        "(", ")",
        "=", "<", ">",
        "==", "<=", ">=",
    ]


def is_space(c) -> bool:
    return c in spaces()


def is_digit(c) -> bool:
    return c in digits()


def is_letter(c) -> bool:
    return c in letters()


def is_symbol(c) -> bool:
    return c in symbols()


def is_eof(c) -> bool:
    return c == ""


def is_string_begin(c) -> bool:
    return c == "\""


def is_string_end(c) -> bool:
    return c == "\""


class Lexer:
    def __init__(self, path: str):
        self.reader: io.FileIO = io.FileIO(path)

        self.cache_last_char: str = ""

        self.cache_next_token: t.Optional[Token] = None

    def next_char(self) -> str:
        if self.cache_last_char != "":
            c = self.cache_last_char
            self.cache_last_char = ""
            return c
        else:
            return self.reader.read(1).decode("utf-8")

    def peek_char(self) -> str:
        if self.cache_last_char != "":
            return self.cache_last_char
        else:
            c = self.next_char()
            self.cache_last_char = c
            return c

    def skip_blank(self):
        c = self.peek_char()
        while is_space(c):
            self.next_char()
            c = self.peek_char()

    def num(self) -> str:
        r = ""
        while True:
            r += self.next_char()
            c = self.peek_char()
            if not (is_digit(c) or c == "."):
                break
        return r

    def name(self) -> str:
        r = ""
        while True:
            r += self.next_char()
            c = self.peek_char()
            if not (is_letter(c) or is_digit(c)):
                break
        return r

    def symbol(self) -> str:
        r = self.next_char()
        c = self.peek_char()
        if is_symbol(r + c):
            c = self.next_char()
            r = r + c
            return r
        else:
            return r

    def string(self) -> str:
        self.next_char()
        r = ""
        c = self.peek_char()
        while not is_string_end(c):
            r += self.next_char()
            c = self.peek_char()
        self.next_char()
        return r

    def next_token(self) -> t.Optional[Token]:
        if self.cache_next_token is not None:
            token = self.cache_next_token
            self.cache_next_token = None
            return token

        # 跳过空白
        self.skip_blank()

        c = self.peek_char()
        if is_eof(c):
            return None
        elif is_digit(c):
            num = self.num()
            if "." in num:
                return FloatToken(num)
            else:
                return IntToken(num)
        elif is_letter(c):
            name = self.name()
            if name in ["true", "false"]:
                return BoolToken(name)
            else:
                return IdentifierToken(name)
        elif is_symbol(c):
            return SymbolToken(self.symbol())
        elif is_string_begin(c):
            return StringToken(self.string())
        else:
            raise ValueError(f"Lexer, 2, c: ({c})")

    def next_token_with_check(self, text):
        token = self.next_token()
        a = token.is_identifier() or token.is_symbol()
        b = text == token.get_text()
        if not (a and b):
            raise ValueError(f'Lexer, 3, token: ({token}), text: ({text})')
        return token

    def next_token_check_identifier(self):
        token = self.next_token()
        if not (token.is_identifier()):
            raise ValueError(f'Lexer, 4, token: ({token})')
        return token

    def peek_token(self) -> t.Optional[Token]:
        if self.cache_next_token is not None:
            token = self.cache_next_token
            return token
        else:
            token = self.next_token()
            self.cache_next_token = token
            return token

    def peek_token_with_judge(self, text) -> bool:
        token = self.peek_token()
        a = token is not None
        b = token.is_identifier() or token.is_symbol()
        c = text == token.get_text()
        return a and b and c

    def peek_token_is_identifier(self) -> bool:
        token = self.peek_token()
        return token is not None and token.is_identifier()
