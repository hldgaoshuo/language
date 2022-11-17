class Token:
    def __init__(self, text):
        self.text = text

    def is_identifier(self):
        return False

    def is_symbol(self):
        return False

    def is_int(self):
        return False

    def is_float(self):
        return False

    def is_bool(self):
        return False

    def is_string(self):
        return False

    def get_int(self):
        raise ValueError("Token, not int token")

    def get_float(self):
        raise ValueError("Token, not float token")

    def get_bool(self):
        raise ValueError("Token, not bool token")

    def get_text(self):
        return ""

    def __str__(self):
        return f'{self.__class__.__name__}({self.text})'

    def __repr__(self):
        return self.__str__()


class IdentifierToken(Token):
    def __init__(self, text):
        super().__init__(text)

    def is_identifier(self):
        return True

    def get_text(self):
        return self.text


class SymbolToken(Token):
    def __init__(self, text):
        super().__init__(text)

    def is_symbol(self):
        return True

    def get_text(self):
        return self.text


class IntToken(Token):
    def __init__(self, text):
        super().__init__(text)

    def is_int(self):
        return True

    def get_int(self):
        return int(self.text)

    def get_text(self):
        return self.text


class FloatToken(Token):
    def __init__(self, text):
        super().__init__(text)

    def is_float(self):
        return True

    def get_float(self):
        return float(self.text)

    def get_text(self):
        return self.text


class BoolToken(Token):
    def __init__(self, text):
        super().__init__(text)

    def is_bool(self):
        return True

    def get_bool(self):
        if self.text == "true":
            return True
        elif self.text == "false":
            return False
        else:
            raise ValueError(f"BoolToken, not bool token: ({self.text})")

    def get_text(self):
        return self.text


class StringToken(Token):
    def __init__(self, text):
        super().__init__(text)

    def is_string(self):
        return True

    def get_text(self):
        return self.text
