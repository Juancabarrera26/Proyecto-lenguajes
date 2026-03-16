# Generated from JCDS.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JCDSParser import JCDSParser
else:
    from JCDSParser import JCDSParser

# This class defines a complete generic visitor for a parse tree produced by JCDSParser.

class JCDSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JCDSParser#program.
    def visitProgram(self, ctx:JCDSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JCDSParser#statement.
    def visitStatement(self, ctx:JCDSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JCDSParser#assignment.
    def visitAssignment(self, ctx:JCDSParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JCDSParser#expression.
    def visitExpression(self, ctx:JCDSParser.ExpressionContext):
        return self.visitChildren(ctx)



del JCDSParser