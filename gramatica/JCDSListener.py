# Generated from JCDS.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JCDSParser import JCDSParser
else:
    from JCDSParser import JCDSParser

# This class defines a complete listener for a parse tree produced by JCDSParser.
class JCDSListener(ParseTreeListener):

    # Enter a parse tree produced by JCDSParser#program.
    def enterProgram(self, ctx:JCDSParser.ProgramContext):
        pass

    # Exit a parse tree produced by JCDSParser#program.
    def exitProgram(self, ctx:JCDSParser.ProgramContext):
        pass


    # Enter a parse tree produced by JCDSParser#statement.
    def enterStatement(self, ctx:JCDSParser.StatementContext):
        pass

    # Exit a parse tree produced by JCDSParser#statement.
    def exitStatement(self, ctx:JCDSParser.StatementContext):
        pass


    # Enter a parse tree produced by JCDSParser#assignment.
    def enterAssignment(self, ctx:JCDSParser.AssignmentContext):
        pass

    # Exit a parse tree produced by JCDSParser#assignment.
    def exitAssignment(self, ctx:JCDSParser.AssignmentContext):
        pass


    # Enter a parse tree produced by JCDSParser#expression.
    def enterExpression(self, ctx:JCDSParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JCDSParser#expression.
    def exitExpression(self, ctx:JCDSParser.ExpressionContext):
        pass



del JCDSParser