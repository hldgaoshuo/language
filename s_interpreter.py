from enum import Enum, auto

from s_exp_bin_op import *
from s_exp_call import *
from s_exp_function import *
from s_exp_closure import *
from s_exp_variable import *
from s_exp_let import *
from s_exp_set import *
from s_exp_if import *
from s_exp_while import *
from s_exp_break import *
from s_exp_continue import *
from s_exp_build_in_log import *
from s_env import *
from utils import log


y_exp = function(
            "f",
            call(
                function(
                    "x",
                    call(
                        variable("f"),
                        function(
                            "v",
                            call(
                                call(
                                    variable("x"),
                                    variable("x")
                                ),
                                variable("v")
                            )
                        )
                    )
                ),
                function(
                    "x",
                    call(
                        variable("f"),
                        function(
                            "v",
                            call(
                                call(
                                    variable("x"),
                                    variable("x")
                                ),
                                variable("v")
                            )
                        )
                    )
                )
            )
        )


class ReturnType(Enum):
    Normal = auto()
    Break = auto()
    Continue = auto()


class Interpreter:
    def __init__(self):
        self.sto = [0] * 1024
        self.sti = 0

    def run(self, exp, env):
        return self.run_(exp, env)

    def run_(self, exp, env):
        if isinstance(exp, int) or isinstance(exp, str) or isinstance(exp, bool) or isinstance(exp, float):
            return exp, ReturnType.Normal
        elif is_bin_op(exp):
            op = bin_op_op(exp)
            if op == "+":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 + e2, ReturnType.Normal
            elif op == "-":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 - e2, ReturnType.Normal
            elif op == "*":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 * e2, ReturnType.Normal
            elif op == "/":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 / e2, ReturnType.Normal
            elif op == "%":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 % e2, ReturnType.Normal
            elif op == "<":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 < e2, ReturnType.Normal
            elif op == ">":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 > e2, ReturnType.Normal
            elif op == "==":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 == e2, ReturnType.Normal
            elif op == ">=":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 >= e2, ReturnType.Normal
            elif op == "<=":
                e1, _ = self.run_(bin_op_e1(exp), env)
                e2, _ = self.run_(bin_op_e2(exp), env)
                return e1 <= e2, ReturnType.Normal
            else:
                raise ValueError(f'Unsupported bin op op: ({op})')
        elif is_variable(exp):
            name = variable_name(exp)
            temp = lookup_env(name, env)
            if temp is None:
                raise ValueError(f'Undefined variable: ({name})')
            if is_closure(temp):
                value = temp
                return value, ReturnType.Normal
            else:
                address = temp
                value = self.sto[address]
                if value is None:
                    raise ValueError(f'Undefined variable: ({name})')
                else:
                    return value, ReturnType.Normal
        elif is_function(exp):
            return closure(exp, env), ReturnType.Normal
        elif is_call(exp):
            op, _ = self.run_(call_op(exp), env)
            if call_arg(exp) is None:
                arg, _ = None, ReturnType.Normal
            else:
                arg, _ = self.run_(call_arg(exp), env)
            if is_closure(op):
                f = closure_fun(op)
                if arg is None:
                    env_ = closure_env(op)
                else:
                    env_ = extend_env(fun_param(f), self.sti, closure_env(op))
                    self.sto[self.sti] = arg
                    self.sti += 1
                return self.run_(fun_body(f), env_)
            else:
                raise ValueError(f'Calling non-function')
        elif is_let(exp):
            name = let_name(exp)
            value, _ = self.run_(let_value(exp), env)
            if is_closure(value):
                env_ = extend_env(name, value, env)
            else:
                env_ = extend_env(name, self.sti, env)
                self.sto[self.sti] = value
                self.sti += 1
            return self.run_(let_body(exp), env_)
        elif is_set(exp):
            value, _ = self.run_(set_value(exp), env)
            name = set_name(exp)
            address = lookup_env(name, env)
            self.sto[address] = value
            if set_body(exp) is None:
                return None, ReturnType.Normal
            else:
                return self.run_(set_body(exp), env)
        elif is_if(exp):
            cond, _ = self.run_(if_cond(exp), env)
            if isinstance(cond, bool):
                if cond:
                    result, return_type = self.run_(if_then(exp), env)
                elif if_else_exp(exp) is not None:
                    result, return_type = self.run_(if_else_exp(exp), env)
                else:
                    result, return_type = None, ReturnType.Normal
                if if_final(exp) is None:
                    return result, return_type
                else:
                    return self.run_(if_final(exp), env)
            else:
                raise ValueError(f'If cond not boolean')
        elif is_break(exp):
            return None, ReturnType.Break
        elif is_continue(exp):
            return None, ReturnType.Continue
        elif is_while(exp):
            cond, _ = self.run_(while_cond(exp), env)
            if isinstance(cond, bool):
                while cond:
                    result, return_type = self.run_(while_then(exp), env)
                    if return_type == ReturnType.Break:
                        break
                    elif return_type == ReturnType.Continue:
                        continue
                    cond, _ = self.run_(while_cond(exp), env)
                return self.run_(while_final(exp), env)
            else:
                raise ValueError(f'While cond not boolean')
        elif is_log(exp):
            arg, _ = self.run_(log_arg(exp), env)
            log(arg)
            if log_final(exp) is None:
                return None, ReturnType.Normal
            else:
                return self.run_(log_final(exp), env)
        else:
            raise ValueError(f'Unsupported exp: ({exp})')
