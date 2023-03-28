class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f"Token({self.token_type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()