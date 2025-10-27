from compiladorVisitor import compiladorVisitor
from compiladorParser import compiladorParser

class Caminante (compiladorVisitor) :
    instr = 0
    hojas = 0

    def visitPrograma (self, ctx:compiladorParser.ProgramaContext):
        print("Programa procesado")
        return self.visitChildren(ctx)
    
    # def visitAsignacion (self, ctx:compiladorParser.AsignacionContext):
    #     print("Asignacion " + str(self.instr))
    #     print("\t" + ctx.getText())
    #     return self.visitChildren(ctx)

    # def visitDeclaracion(self, ctx:compiladorParser.DeclaracionContext):
    #     print("Declaracion " + str(self.instr))
    #     print("\t" + ctx.getText())
    #     return self.visitChildren(ctx)

    # def visitInstruccion(self, ctx:compiladorParser.InstruccionContext):
    #     self.instr += 1
    #     print("Instruccion " + str(self.instr))
    #     print("\t" + ctx.getText())
    #     return self.visitChildren(ctx)

    def visitIwhile(self, ctx:compiladorParser.IwhileContext):
        # for i in list(range(ctx.getChildCount())) :
        #     print(self.visitChildren(ctx).getText())
        print("Entro a while")
        return self.visitChildren(ctx.getChild(4))
        # return self.visit(ctx.getChild(4))
        # return self.visitInstruccion(ctx)

    def visitTerminal(self, node):
        # print(node.getText())
        self.hojas += 1
        return super().visitTerminal(node)
    
    def printNumeroHojas (self) :
        print("Hojas " + str(self.hojas))
