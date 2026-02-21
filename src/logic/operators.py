class Eq:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Neq:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Gt:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Lt:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class And:
    def __init__(self, *args):
        self.args = args

class Or:
    def __init__(self, *args):
        self.args = args

class Not:
    def __init__(self, arg):
        self.arg = arg
