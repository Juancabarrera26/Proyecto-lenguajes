from JCDSVisitor import JCDSVisitor


class EvalVisitor(JCDSVisitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx):
        for s in ctx.statement():
            self.visit(s)

    def visitAssignment(self, ctx):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expression())
        self.variables[nombre] = valor
        print(nombre, "=", valor)
        return valor

    def visitExpression(self, ctx):

        # numero
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())

        # variable
        if ctx.ID() and ctx.getChildCount() == 1:
            nombre = ctx.ID().getText()
            if nombre not in self.variables:
                raise Exception("Variable no definida: " + nombre)
            return self.variables[nombre]

        # sqrt(...)
        if ctx.getChildCount() == 4 and ctx.getChild(0).getText() == "sqrt":
            valor = self.visit(ctx.getChild(2))
            return self.sqrt(valor)

        # parentesis
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(":
            return self.visit(ctx.getChild(1))

        # operaciones
        if ctx.getChildCount() == 3:
            izq = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            der = self.visit(ctx.getChild(2))

            if op == "+":
                return izq + der
            if op == "-":
                return izq - der
            if op == "*":
                return izq * der
            if op == "/":
                if der == 0:
                    raise Exception("Division por cero")
                return izq / der
            if op == "^":
                return izq ** der

    def sqrt(self, n):
        if n < 0:
            raise Exception("No se puede sacar raiz cuadrada de un numero negativo")

        if n == 0:
            return 0

        x = n
        for _ in range(20):
            x = 0.5 * (x + n / x)

        return x