class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return str(self.value)
    

class Integer(Token): #inherited from Token
    def __init__(self,value):
        super().__init__("INT", value)

class Float(Token):  #inherited from Token
    def __init__(self, value):
        super().__init__("FLT", value)

class Operation(Token):  #inherited from Token
    def __init__(self, value):
        super().__init__("OP", value)

class Declaration(Token):
    def __init__(self,value):
        super().__init__("DECL", value)

class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR(?)", value)