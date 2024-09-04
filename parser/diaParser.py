# Generated from dia.g4 by ANTLR 4.13.2
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
        4,1,11,32,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,1,0,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,30,8,2,1,2,0,0,3,0,2,4,0,0,35,0,9,1,0,0,0,2,14,1,
        0,0,0,4,29,1,0,0,0,6,8,3,4,2,0,7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,
        0,0,9,10,1,0,0,0,10,12,1,0,0,0,11,9,1,0,0,0,12,13,5,0,0,1,13,1,1,
        0,0,0,14,18,5,1,0,0,15,17,3,4,2,0,16,15,1,0,0,0,17,20,1,0,0,0,18,
        16,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,18,1,0,0,0,21,22,5,2,0,
        0,22,3,1,0,0,0,23,30,5,11,0,0,24,30,5,8,0,0,25,30,5,9,0,0,26,30,
        5,10,0,0,27,30,3,2,1,0,28,30,5,5,0,0,29,23,1,0,0,0,29,24,1,0,0,0,
        29,25,1,0,0,0,29,26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,5,1,0,
        0,0,3,9,18,29
    ]

class diaParser ( Parser ):

    grammarFileName = "dia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'''", "'\"'", "';'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                      "SEMICOLON", "LINEBREAK", "WS", "STRING_SINGLE", "STRING_DOUBLE", 
                      "DICTIONARY", "CODE" ]

    RULE_rule_set = 0
    RULE_nestedStatements = 1
    RULE_statements = 2

    ruleNames =  [ "rule_set", "nestedStatements", "statements" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    SINGLE_QUOTE=3
    DOUBLE_QUOTE=4
    SEMICOLON=5
    LINEBREAK=6
    WS=7
    STRING_SINGLE=8
    STRING_DOUBLE=9
    DICTIONARY=10
    CODE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Rule_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(diaParser.EOF, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diaParser.StatementsContext)
            else:
                return self.getTypedRuleContext(diaParser.StatementsContext,i)


        def getRuleIndex(self):
            return diaParser.RULE_rule_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_set" ):
                listener.enterRule_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_set" ):
                listener.exitRule_set(self)




    def rule_set(self):

        localctx = diaParser.Rule_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rule_set)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3874) != 0):
                self.state = 6
                self.statements()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(diaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NestedStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(diaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(diaParser.RPAREN, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diaParser.StatementsContext)
            else:
                return self.getTypedRuleContext(diaParser.StatementsContext,i)


        def getRuleIndex(self):
            return diaParser.RULE_nestedStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedStatements" ):
                listener.enterNestedStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedStatements" ):
                listener.exitNestedStatements(self)




    def nestedStatements(self):

        localctx = diaParser.NestedStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nestedStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(diaParser.LPAREN)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3874) != 0):
                self.state = 15
                self.statements()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(diaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE(self):
            return self.getToken(diaParser.CODE, 0)

        def STRING_SINGLE(self):
            return self.getToken(diaParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(diaParser.STRING_DOUBLE, 0)

        def DICTIONARY(self):
            return self.getToken(diaParser.DICTIONARY, 0)

        def nestedStatements(self):
            return self.getTypedRuleContext(diaParser.NestedStatementsContext,0)


        def SEMICOLON(self):
            return self.getToken(diaParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return diaParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = diaParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statements)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(diaParser.CODE)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(diaParser.STRING_SINGLE)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(diaParser.STRING_DOUBLE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(diaParser.DICTIONARY)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 5)
                self.state = 27
                self.nestedStatements()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 28
                self.match(diaParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





