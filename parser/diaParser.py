# Generated from C:/Users/Julian/compilerbau-dhbw-4/CompilerbauSemester4/parser/dia.g4 by ANTLR 4.13.2
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
        4,1,13,51,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,
        9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,49,8,4,1,4,0,0,5,0,2,4,6,8,0,
        2,1,0,11,12,1,0,9,12,53,0,13,1,0,0,0,2,18,1,0,0,0,4,29,1,0,0,0,6,
        33,1,0,0,0,8,48,1,0,0,0,10,12,3,8,4,0,11,10,1,0,0,0,12,15,1,0,0,
        0,13,11,1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,
        5,0,0,1,17,1,1,0,0,0,18,19,5,2,0,0,19,24,3,4,2,0,20,21,5,13,0,0,
        21,23,3,4,2,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,
        0,0,0,25,27,1,0,0,0,26,24,1,0,0,0,27,28,5,3,0,0,28,3,1,0,0,0,29,
        30,7,0,0,0,30,31,5,1,0,0,31,32,7,1,0,0,32,5,1,0,0,0,33,37,5,2,0,
        0,34,36,3,8,4,0,35,34,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,3,0,0,41,7,1,0,0,0,42,
        49,3,2,1,0,43,49,5,11,0,0,44,49,5,9,0,0,45,49,5,10,0,0,46,49,3,6,
        3,0,47,49,5,6,0,0,48,42,1,0,0,0,48,43,1,0,0,0,48,44,1,0,0,0,48,45,
        1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,9,1,0,0,0,4,13,24,37,48
    ]

class diaParser ( Parser ):

    grammarFileName = "dia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'{'", "'}'", "'''", "'\"'", "';'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", "SINGLE_QUOTE", 
                      "DOUBLE_QUOTE", "SEMICOLON", "LINEBREAK", "WS", "STRING_SINGLE", 
                      "STRING_DOUBLE", "CODE", "NUMBER", "COMMA" ]

    RULE_rule_set = 0
    RULE_dictionary = 1
    RULE_key_value = 2
    RULE_nestedStatements = 3
    RULE_statements = 4

    ruleNames =  [ "rule_set", "dictionary", "key_value", "nestedStatements", 
                   "statements" ]

    EOF = Token.EOF
    T__0=1
    LPAREN=2
    RPAREN=3
    SINGLE_QUOTE=4
    DOUBLE_QUOTE=5
    SEMICOLON=6
    LINEBREAK=7
    WS=8
    STRING_SINGLE=9
    STRING_DOUBLE=10
    CODE=11
    NUMBER=12
    COMMA=13

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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3652) != 0):
                self.state = 10
                self.statements()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(diaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DictionaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(diaParser.LPAREN, 0)

        def key_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diaParser.Key_valueContext)
            else:
                return self.getTypedRuleContext(diaParser.Key_valueContext,i)


        def RPAREN(self):
            return self.getToken(diaParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(diaParser.COMMA)
            else:
                return self.getToken(diaParser.COMMA, i)

        def getRuleIndex(self):
            return diaParser.RULE_dictionary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDictionary" ):
                listener.enterDictionary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDictionary" ):
                listener.exitDictionary(self)




    def dictionary(self):

        localctx = diaParser.DictionaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dictionary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(diaParser.LPAREN)
            self.state = 19
            self.key_value()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 20
                self.match(diaParser.COMMA)
                self.state = 21
                self.key_value()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.match(diaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE(self, i:int=None):
            if i is None:
                return self.getTokens(diaParser.CODE)
            else:
                return self.getToken(diaParser.CODE, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(diaParser.NUMBER)
            else:
                return self.getToken(diaParser.NUMBER, i)

        def STRING_SINGLE(self):
            return self.getToken(diaParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(diaParser.STRING_DOUBLE, 0)

        def getRuleIndex(self):
            return diaParser.RULE_key_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey_value" ):
                listener.enterKey_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey_value" ):
                listener.exitKey_value(self)




    def key_value(self):

        localctx = diaParser.Key_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_key_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 30
            self.match(diaParser.T__0)
            self.state = 31
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
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
        self.enterRule(localctx, 6, self.RULE_nestedStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(diaParser.LPAREN)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3652) != 0):
                self.state = 34
                self.statements()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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

        def dictionary(self):
            return self.getTypedRuleContext(diaParser.DictionaryContext,0)


        def CODE(self):
            return self.getToken(diaParser.CODE, 0)

        def STRING_SINGLE(self):
            return self.getToken(diaParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(diaParser.STRING_DOUBLE, 0)

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
        self.enterRule(localctx, 8, self.RULE_statements)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.dictionary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(diaParser.CODE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(diaParser.STRING_SINGLE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(diaParser.STRING_DOUBLE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.nestedStatements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.match(diaParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





