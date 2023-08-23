from tokens import Integer,Float,Operation, Declaration, Variable

class Lexer:
    # Class variables
    digits = "0123456789"
    operations = "+-/*()="
    stopwords = [" "]
    letters = "abcdefghijklmnopqrstuvwxyz"
    declarations = ["craft"]

    def __init__(self,text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None

    def tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexer.digits:  #If the current character is a number
                self.token = self.extract_number()

            elif self.char in Lexer.operations: #If the current character is an operator
                self.token = Operation(self.char)
                self.move()

            elif self.char in Lexer.stopwords:
                self.move()
                continue

            elif self.char in Lexer.letters:
                word = self.extract_word()

                if word in Lexer.declarations:
                    self.token = Declaration(word)
                else:
                    self.token = Variable(word)

            self.tokens.append(self.token)
        
        return self.tokens

    def extract_number(self):
        number = ""  # storing numbers as string
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":      # if the number is float
                isFloat = True
            number += self.char
            self.move()
        return Integer(number) if not isFloat else Float(number)

    def extract_word(self):
        word = ""
        while self.char in Lexer.letters and self.idx < len(self.text):
            word += self.char
            self.move()

        return word

    def move(self):
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]

