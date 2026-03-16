import sys
sys.path.append("../gramatica")

from antlr4 import *
from JCDSLexer import JCDSLexer
from JCDSParser import JCDSParser
from visitor import EvalVisitor


def run_file(filename):

    input_stream = FileStream(filename)

    lexer = JCDSLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = JCDSParser(stream)
    tree = parser.program()

    visitor = EvalVisitor()
    visitor.visit(tree)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso: python3 main.py archivo.jcds")
        sys.exit(1)

    run_file(sys.argv[1])
