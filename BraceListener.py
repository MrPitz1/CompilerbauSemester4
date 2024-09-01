# Generated from ./Brace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BraceParser import BraceParser
else:
    from BraceParser import BraceParser

# This class defines a complete listener for a parse tree produced by BraceParser.
class BraceListener(ParseTreeListener):

    # Enter a parse tree produced by BraceParser#rule_set.
    def enterRule_set(self, ctx:BraceParser.Rule_setContext):
        pass

    # Exit a parse tree produced by BraceParser#rule_set.
    def exitRule_set(self, ctx:BraceParser.Rule_setContext):
        pass


    # Enter a parse tree produced by BraceParser#nestedCondition.
    def enterNestedCondition(self, ctx:BraceParser.NestedConditionContext):
        pass

    # Exit a parse tree produced by BraceParser#nestedCondition.
    def exitNestedCondition(self, ctx:BraceParser.NestedConditionContext):
        pass


    # Enter a parse tree produced by BraceParser#statements.
    def enterStatements(self, ctx:BraceParser.StatementsContext):
        pass

    # Exit a parse tree produced by BraceParser#statements.
    def exitStatements(self, ctx:BraceParser.StatementsContext):
        pass



del BraceParser