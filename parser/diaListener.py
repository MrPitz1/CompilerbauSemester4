# Generated from dia.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .diaParser import diaParser
else:
    from diaParser import diaParser

# This class defines a complete listener for a parse tree produced by diaParser.
class diaListener(ParseTreeListener):

    # Enter a parse tree produced by diaParser#rule_set.
    def enterRule_set(self, ctx:diaParser.Rule_setContext):
        pass

    # Exit a parse tree produced by diaParser#rule_set.
    def exitRule_set(self, ctx:diaParser.Rule_setContext):
        pass


    # Enter a parse tree produced by diaParser#dictionary.
    def enterDictionary(self, ctx:diaParser.DictionaryContext):
        pass

    # Exit a parse tree produced by diaParser#dictionary.
    def exitDictionary(self, ctx:diaParser.DictionaryContext):
        pass


    # Enter a parse tree produced by diaParser#pair.
    def enterPair(self, ctx:diaParser.PairContext):
        pass

    # Exit a parse tree produced by diaParser#pair.
    def exitPair(self, ctx:diaParser.PairContext):
        pass


    # Enter a parse tree produced by diaParser#nestedStatements.
    def enterNestedStatements(self, ctx:diaParser.NestedStatementsContext):
        pass

    # Exit a parse tree produced by diaParser#nestedStatements.
    def exitNestedStatements(self, ctx:diaParser.NestedStatementsContext):
        pass


    # Enter a parse tree produced by diaParser#statements.
    def enterStatements(self, ctx:diaParser.StatementsContext):
        pass

    # Exit a parse tree produced by diaParser#statements.
    def exitStatements(self, ctx:diaParser.StatementsContext):
        pass


    # Enter a parse tree produced by diaParser#nesStatements.
    def enterNesStatements(self, ctx:diaParser.NesStatementsContext):
        pass

    # Exit a parse tree produced by diaParser#nesStatements.
    def exitNesStatements(self, ctx:diaParser.NesStatementsContext):
        pass


    # Enter a parse tree produced by diaParser#dicstatements.
    def enterDicstatements(self, ctx:diaParser.DicstatementsContext):
        pass

    # Exit a parse tree produced by diaParser#dicstatements.
    def exitDicstatements(self, ctx:diaParser.DicstatementsContext):
        pass



del diaParser