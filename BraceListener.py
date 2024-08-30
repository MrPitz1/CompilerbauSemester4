# Generated from C:/Users/simon/Documents/hochschule/compiler/CompilerbauSemester4/Brace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BraceParser import BraceParser
else:
    from BraceParser import BraceParser

# This class defines a complete listener for a parse tree produced by BraceParser.
class BraceListener(ParseTreeListener):

    # Enter a parse tree produced by BraceParser#expression.
    def enterExpression(self, ctx:BraceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BraceParser#expression.
    def exitExpression(self, ctx:BraceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BraceParser#nested_content.
    def enterNested_content(self, ctx:BraceParser.Nested_contentContext):
        pass

    # Exit a parse tree produced by BraceParser#nested_content.
    def exitNested_content(self, ctx:BraceParser.Nested_contentContext):
        pass


    # Enter a parse tree produced by BraceParser#identifier.
    def enterIdentifier(self, ctx:BraceParser.IdentifierContext):
        pass

    # Exit a parse tree produced by BraceParser#identifier.
    def exitIdentifier(self, ctx:BraceParser.IdentifierContext):
        pass


    # Enter a parse tree produced by BraceParser#line_end.
    def enterLine_end(self, ctx:BraceParser.Line_endContext):
        pass

    # Exit a parse tree produced by BraceParser#line_end.
    def exitLine_end(self, ctx:BraceParser.Line_endContext):
        pass



del BraceParser