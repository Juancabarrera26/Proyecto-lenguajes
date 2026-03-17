from antlr4 import InputStream, FileStream, CommonTokenStream
from JCDSLexer import JCDSLexer
from JCDSParser import JCDSParser
from visitor import EvalVisitor


def ejecutar_texto(texto, visitor):
    entrada = InputStream(texto)
    lexer = JCDSLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = JCDSParser(tokens)
    arbol = parser.program()
    visitor.visit(arbol)


def ejecutar_archivo(ruta, visitor):
    entrada = FileStream(ruta, encoding="utf-8")
    lexer = JCDSLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = JCDSParser(tokens)
    arbol = parser.program()
    visitor.visit(arbol)


visitor = EvalVisitor()

print("JCDS - Modo interactivo")
print("Escribe 'salir' para terminar\n")

while True:
    texto = input(">>> ")

    if texto.lower() == "salir":
        break

    try:
        ejecutar_texto(texto, visitor)
    except Exception as e:
        print("Error:", e)
