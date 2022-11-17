from s_lexer import Lexer
from utils import log


def test1():
    lexer = Lexer("a.js")
    tokens = []
    token = lexer.next_token()
    while token is not None:
        tokens.append(token)
        token = lexer.next_token()
    log(tokens)


def test2():
    lexer = Lexer("b.js")
    tokens = []
    token = lexer.next_token()
    while token is not None:
        tokens.append(token)
        token = lexer.next_token()
    log(tokens)


if __name__ == '__main__':
    test1()
    test2()
