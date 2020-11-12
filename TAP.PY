#Essa será a classe criada que conterá as verificações:

import ply.lex as lex

class TAP:

    def t_error(self, t):
        raise Exception("Not recognized: %s" % t.value)

    def __init__(self):
        self.lexer = None

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def execute(self, query):
        self.lexer.input(query)

