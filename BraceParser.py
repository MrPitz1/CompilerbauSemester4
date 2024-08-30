# Generated from C:/Users/simon/Documents/hochschule/compiler/CompilerbauSemester4/Brace.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,5,0,11,8,0,10,0,
        12,0,14,9,0,1,0,3,0,17,8,0,1,0,1,0,5,0,21,8,0,10,0,12,0,24,9,0,1,
        1,1,1,1,1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,2,1,2,1,3,1,
        3,1,3,0,0,4,0,2,4,6,0,1,1,0,1,3,44,0,12,1,0,0,0,2,25,1,0,0,0,4,36,
        1,0,0,0,6,38,1,0,0,0,8,11,3,4,2,0,9,11,3,6,3,0,10,8,1,0,0,0,10,9,
        1,0,0,0,11,14,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,16,1,0,0,0,
        14,12,1,0,0,0,15,17,3,2,1,0,16,15,1,0,0,0,16,17,1,0,0,0,17,22,1,
        0,0,0,18,21,3,4,2,0,19,21,3,6,3,0,20,18,1,0,0,0,20,19,1,0,0,0,21,
        24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,1,1,0,0,0,24,22,1,0,0,
        0,25,31,5,4,0,0,26,30,3,4,2,0,27,30,3,2,1,0,28,30,3,6,3,0,29,26,
        1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,
        31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,5,0,0,35,3,1,0,
        0,0,36,37,5,6,0,0,37,5,1,0,0,0,38,39,7,0,0,0,39,7,1,0,0,0,7,10,12,
        16,20,22,29,31
    ]

class BraceParser ( Parser ):

    grammarFileName = "Brace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\r\\n'", "'\\r'", "'\\n'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Lbrace", "Rbrace", "WORD", "WS" ]

    RULE_expression = 0
    RULE_nested_content = 1
    RULE_identifier = 2
    RULE_line_end = 3

    ruleNames =  [ "expression", "nested_content", "identifier", "line_end" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Lbrace=4
    Rbrace=5
    WORD=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BraceParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(BraceParser.IdentifierContext,i)


        def line_end(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BraceParser.Line_endContext)
            else:
                return self.getTypedRuleContext(BraceParser.Line_endContext,i)


        def nested_content(self):
            return self.getTypedRuleContext(BraceParser.Nested_contentContext,0)


        def getRuleIndex(self):
            return BraceParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = BraceParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 10
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [6]:
                        self.state = 8
                        self.identifier()
                        pass
                    elif token in [1, 2, 3]:
                        self.state = 9
                        self.line_end()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 14
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 15
                self.nested_content()


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 78) != 0):
                self.state = 20
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 18
                    self.identifier()
                    pass
                elif token in [1, 2, 3]:
                    self.state = 19
                    self.line_end()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nested_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lbrace(self):
            return self.getToken(BraceParser.Lbrace, 0)

        def Rbrace(self):
            return self.getToken(BraceParser.Rbrace, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BraceParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(BraceParser.IdentifierContext,i)


        def nested_content(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BraceParser.Nested_contentContext)
            else:
                return self.getTypedRuleContext(BraceParser.Nested_contentContext,i)


        def line_end(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BraceParser.Line_endContext)
            else:
                return self.getTypedRuleContext(BraceParser.Line_endContext,i)


        def getRuleIndex(self):
            return BraceParser.RULE_nested_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNested_content" ):
                listener.enterNested_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNested_content" ):
                listener.exitNested_content(self)




    def nested_content(self):

        localctx = BraceParser.Nested_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nested_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(BraceParser.Lbrace)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 94) != 0):
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 26
                    self.identifier()
                    pass
                elif token in [4]:
                    self.state = 27
                    self.nested_content()
                    pass
                elif token in [1, 2, 3]:
                    self.state = 28
                    self.line_end()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(BraceParser.Rbrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(BraceParser.WORD, 0)

        def getRuleIndex(self):
            return BraceParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = BraceParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(BraceParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BraceParser.RULE_line_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_end" ):
                listener.enterLine_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_end" ):
                listener.exitLine_end(self)




    def line_end(self):

        localctx = BraceParser.Line_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_line_end)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





