from s_exp_bin_op import *
from s_exp_let import *
from s_exp_function import *
from s_exp_call import *
from s_exp_variable import *
from s_exp_set import *
from s_exp_if import *
from s_exp_while import *
from s_exp_break import *
from s_exp_continue import *
from s_exp_build_in_log import *
from utils import log


class Precedence:
    def __init__(self, value, is_left_associative):
        self.value = value  # value 越大，优先级越高
        self.is_left_associative = is_left_associative


def is_right_associative(precedence, next_precedence):
    if next_precedence.is_left_associative:
        return precedence.value < next_precedence.value
    else:
        return precedence.value <= next_precedence.value


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.operators = {
            "==": Precedence(1, True),
            "<=": Precedence(1, True),
            ">=": Precedence(1, True),
            "<": Precedence(2, True),
            ">": Precedence(2, True),
            "+": Precedence(3, True),
            "-": Precedence(3, True),
            "*": Precedence(4, True),
            "/": Precedence(4, True),
            "%": Precedence(4, True),
            "^": Precedence(5, False),  # 使用示范，暂时用不到这个运算符
        }

    def program(self):
        return self.expression()

    # expression 所需的辅助函数
    def shift(self, left, precedence):
        t = self.lexer.next_token()
        op = t.get_text()

        right = self.factor()

        t = self.lexer.peek_token()
        if t is not None and t.is_symbol():
            p = self.operators.get(t.get_text())
            if p is not None and is_right_associative(precedence, p):
                right = self.shift(right, p)

        return bin_op(op, left, right)

    def expression(self):
        if self.lexer.peek_token_with_judge("let"):
            self.lexer.next_token_with_check("let")
            name = self.primary()
            self.lexer.next_token_with_check("=")
            value = self.expression()
            body = self.expression()
            return let(name, value, body)
        elif self.lexer.peek_token_with_judge("function"):
            self.lexer.next_token_with_check("function")
            self.lexer.next_token_with_check("(")
            if self.lexer.peek_token_with_judge(")"):
                self.lexer.next_token_with_check(")")
                param = None
            else:
                param = self.primary()
                if self.lexer.peek_token_with_judge(")"):
                    self.lexer.next_token_with_check(")")
            return function(param, self.expression())
        elif self.lexer.peek_token_with_judge("if"):
            self.lexer.next_token_with_check("if")
            self.lexer.next_token_with_check("(")
            cond = self.expression()
            self.lexer.next_token_with_check(")")
            then = self.expression()
            if self.lexer.peek_token_with_judge("else"):
                self.lexer.next_token_with_check("else")
                else_exp = self.expression()
            else:
                else_exp = None
            if self.lexer.peek_token_with_judge("}"):
                final = None
            else:
                final = self.expression()
            return if_exp(cond, then, else_exp, final)
        elif self.lexer.peek_token_with_judge("while"):
            self.lexer.next_token_with_check("while")
            self.lexer.next_token_with_check("(")
            cond = self.expression()
            self.lexer.next_token_with_check(")")
            then = self.expression()
            final = self.expression()
            return while_exp(cond, then, final)
        elif self.lexer.peek_token_with_judge("log"):
            self.lexer.next_token_with_check("log")
            self.lexer.next_token_with_check("(")
            arg = self.expression()
            self.lexer.next_token_with_check(")")
            if self.lexer.peek_token_with_judge("}"):
                final = None
            else:
                final = self.expression()
            return log_exp(arg, final)
        elif self.lexer.peek_token_with_judge("break"):
            self.lexer.next_token_with_check("break")
            return break_exp()
        elif self.lexer.peek_token_with_judge("continue"):
            self.lexer.next_token_with_check("continue")
            return continue_exp()
        elif self.lexer.peek_token_with_judge("{"):
            self.lexer.next_token_with_check("{")
            body = self.expression()
            self.lexer.next_token_with_check("}")
            return body
        elif self.lexer.peek_token_with_judge(","):
            self.lexer.next_token_with_check(",")
            param = self.primary()
            if self.lexer.peek_token_with_judge(")"):
                self.lexer.next_token_with_check(")")
                body = self.expression()
                return function(param, body)
            else:
                return function(param, self.expression())
        else:
            right = self.factor()
            if self.lexer.peek_token_with_judge("("):
                self.lexer.next_token_with_check("(")
                if self.lexer.peek_token_with_judge(")"):
                    arg = None
                else:
                    arg = self.expression()
                result = call(right, arg)
                while self.lexer.peek_token_with_judge(","):
                    self.lexer.next_token_with_check(",")
                    arg = self.expression()
                    result = call(result, arg)
                self.lexer.next_token_with_check(")")
                return result
            elif self.lexer.peek_token_with_judge("="):
                self.lexer.next_token_with_check("=")
                value = self.expression()
                if self.lexer.peek_token_with_judge("}"):
                    body = None
                else:
                    body = self.expression()
                return set_exp(right, value, body)
            else:
                t = self.lexer.peek_token()
                while t is not None and t.is_symbol():
                    p = self.operators.get(t.get_text())
                    if p is None:
                        break
                    right = self.shift(right, p)
                    t = self.lexer.peek_token()
                return right

    def factor(self):
        if self.lexer.peek_token_with_judge("-"):
            self.lexer.next_token_with_check("-")
            f = self.primary()
            if isinstance(f, int) or isinstance(f, float):
                return bin_op("-", 0, f)
            elif isinstance(f, str):
                return bin_op("-", 0, variable(f))
            else:
                return bin_op("-", 0, f)
        elif self.lexer.peek_token_is_identifier():
            f = self.primary()
            if self.lexer.peek_token_with_judge("="):
                return f
            else:
                return variable(f)
        else:
            f = self.primary()
            return f

    def primary(self):
        if self.lexer.peek_token_with_judge("("):
            self.lexer.next_token_with_check("(")
            e = self.expression()
            self.lexer.next_token_with_check(")")
            return e
        else:
            t = self.lexer.next_token()
            if t.is_int():
                return t.get_int()
            elif t.is_float():
                return t.get_float()
            elif t.is_bool():
                return t.get_bool()
            elif t.is_identifier():
                return t.get_text()
            elif t.is_symbol():
                return t.get_text()
            elif t.is_string():
                return t.get_text()
            else:
                raise ValueError(f"Parser, 2")
