from antlr4 import FileStream, CommonTokenStream
from JCDSLexer import JCDSLexer
from JCDSParser import JCDSParser
from visitor import EvalVisitor


archivo = input("Ingrese el nombre del archivo .jcds: ")

entrada = FileStream(archivo, encoding="utf-8")
lexer = JCDSLexer(entrada)
tokens = CommonTokenStream(lexer)
parser = JCDSParser(tokens)
arbol = parser.program()

visitor = EvalVisitor()
visitor.visit(arbol)