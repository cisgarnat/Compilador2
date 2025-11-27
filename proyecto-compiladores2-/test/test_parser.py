from antlr4 import *
from ConsultaSQLLexer import ConsultaSQLLexer
from ConsultaSQLParser import ConsultaSQLParser


def test_parse_mostrar():
    entrada = InputStream("MOSTRAR PRODUCTOS")
    lexer = ConsultaSQLLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = ConsultaSQLParser(tokens)

    tree = parser.consulta()

    assert tree is not None  # No generó error
