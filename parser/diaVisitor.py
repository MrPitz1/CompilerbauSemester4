# Generated from ./dia.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .diaParser import diaParser
else:
    from diaParser import diaParser

# This class defines a complete generic visitor for a parse tree produced by diaParser.

class diaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by diaParser#rule_set.
    def visitRule_set(self, ctx:diaParser.Rule_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by diaParser#nestedStatements.
    def visitNestedStatements(self, ctx:diaParser.NestedStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by diaParser#statements.
    def visitStatements(self, ctx:diaParser.StatementsContext):
        return self.visitChildren(ctx)



del diaParser