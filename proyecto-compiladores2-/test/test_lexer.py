from antlr4 import InputStream, CommonTokenStream
from ConsultaSQLLexer import ConsultaSQLLexer

def test_tokens_mostrar():
    entrada = InputStream("MOSTRAR PRODUCTOS")
    lexer = ConsultaSQLLexer(entrada)
    tokens = [t.text for t in lexer.getAllTokens()]

    assert "MOSTRAR" in tokens
    assert "PRODUCTOS" in tokens
