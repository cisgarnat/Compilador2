from antlr4 import *
from ConsultaSQLLexer import ConsultaSQLLexer
from ConsultaSQLParser import ConsultaSQLParser
from ConsultaSQLVisitor import ConsultaSQLVisitor

class TestVisitor(ConsultaSQLVisitor):
    pass

def test_traduccion_mostrar():
    entrada = InputStream("MOSTRAR PRODUCTOS")
    lexer = ConsultaSQLLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = ConsultaSQLParser(tokens)
    tree = parser.consulta()

    visitor = ConsultaSQLVisitor()
    resultado = visitor.visit(tree)

    assert resultado == "SELECT * FROM PRODUCTOS;"
