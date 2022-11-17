from s_lexer import Lexer
from s_parser import Parser
from s_interpreter import Interpreter
from utils import ensure_equal, log


def test1():
    lexer = Lexer("a.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(339159, result[0])


def test2():
    lexer = Lexer("b.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(17.77777777777778, result[0])


def test3():
    lexer = Lexer("c.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(98.07795077187492, result[0])


def test4():
    lexer = Lexer("d.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(-1, result[0])


def test5():
    lexer = Lexer("e.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(-3.2, result[0])


def test6():
    lexer = Lexer("f.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(-1, result[0])


def test7():
    lexer = Lexer("g.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(False, result[0])


def test8():
    lexer = Lexer("h.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(5050, result[0])


def test9():
    lexer = Lexer("aa.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal("abcdefghi", result[0])


def test10():
    lexer = Lexer("i.js")
    parser = Parser(lexer)
    interpreter = Interpreter()
    exp = parser.program()
    env = {}
    result = interpreter.run(exp, env)
    ensure_equal(None, result[0])


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
