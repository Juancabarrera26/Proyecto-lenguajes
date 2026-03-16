import sys
sys.path.append("../gramatica")

from JCDSVisitor import JCDSVisitor


class EvalVisitor(JCDSVisitor):

    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expression())

        self.memory[name] = value

        print(name, "=", value)

        return value

    def visitExpression(self, ctx):

        if ctx.getChildCount() == 3:

            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if op == '+':
                return left + right

            if op == '-':
                return left - right

            if op == '*':
                return left * right

            if op == '/':
                return left / right

            if op == '^':
                return left ** right

        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())

        if ctx.ID():
            name = ctx.ID().getText()
            return self.memory.get(name, 0)

        return self.visitChildren(ctx)
