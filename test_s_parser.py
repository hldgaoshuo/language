from s_lexer import Lexer
from s_parser import Parser
from s_pair import pair_to_string
from utils import log


def test1():
    lexer = Lexer("a.js")
    parser = Parser(lexer)
    r = parser.program()
    log(pair_to_string(r))


def test2():
    lexer = Lexer("b.js")
    parser = Parser(lexer)
    r = parser.program()
    log(pair_to_string(r))


if __name__ == '__main__':
    test1()
    test2()
