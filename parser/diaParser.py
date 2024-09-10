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
        4,1,13,78,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,3,1,26,8,1,
        1,1,1,1,1,1,1,1,1,2,3,2,33,8,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,4,
        3,43,8,3,11,3,12,3,44,4,3,47,8,3,11,3,12,3,48,1,4,1,4,1,4,5,4,54,
        8,4,10,4,12,4,57,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,67,8,5,
        1,6,1,6,1,6,1,6,1,6,3,6,74,8,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,
        14,0,1,1,0,10,12,86,0,19,1,0,0,0,2,25,1,0,0,0,4,32,1,0,0,0,6,46,
        1,0,0,0,8,50,1,0,0,0,10,66,1,0,0,0,12,73,1,0,0,0,14,75,1,0,0,0,16,
        18,3,10,5,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,
        0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,26,
        5,13,0,0,25,24,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,1,0,0,
        28,29,3,6,3,0,29,30,5,2,0,0,30,3,1,0,0,0,31,33,5,13,0,0,32,31,1,
        0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,5,1,0,0,35,36,3,6,3,0,36,
        37,5,2,0,0,37,5,1,0,0,0,38,39,3,14,7,0,39,42,5,5,0,0,40,43,3,14,
        7,0,41,43,3,4,2,0,42,40,1,0,0,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,
        1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,38,1,0,0,0,47,48,1,0,0,0,
        48,46,1,0,0,0,48,49,1,0,0,0,49,7,1,0,0,0,50,55,5,1,0,0,51,54,3,2,
        1,0,52,54,3,12,6,0,53,51,1,0,0,0,53,52,1,0,0,0,54,57,1,0,0,0,55,
        53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,2,0,
        0,59,9,1,0,0,0,60,67,5,12,0,0,61,67,5,10,0,0,62,67,5,11,0,0,63,67,
        3,8,4,0,64,67,3,2,1,0,65,67,5,7,0,0,66,60,1,0,0,0,66,61,1,0,0,0,
        66,62,1,0,0,0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,11,1,
        0,0,0,68,74,5,12,0,0,69,74,5,10,0,0,70,74,5,11,0,0,71,74,3,8,4,0,
        72,74,5,7,0,0,73,68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,
        0,0,0,73,72,1,0,0,0,74,13,1,0,0,0,75,76,7,0,0,0,76,15,1,0,0,0,10,
        19,25,32,42,44,48,53,55,66,73
    ]

class diaParser ( Parser ):

    grammarFileName = "dia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'''", "'\"'", "':'", "'='", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "SINGLE_QUOTE", "DOUBLE_QUOTE", 
                      "COLON", "EQUALS", "SEMICOLON", "LINEBREAK", "WS", 
                      "STRING_SINGLE", "STRING_DOUBLE", "CODE", "VARIABLE" ]

    RULE_rule_set = 0
    RULE_dictionary = 1
    RULE_nesteddictionary = 2
    RULE_pair = 3
    RULE_nestedStatements = 4
    RULE_statements = 5
    RULE_nesStatements = 6
    RULE_dicstatements = 7

    ruleNames =  [ "rule_set", "dictionary", "nesteddictionary", "pair", 
                   "nestedStatements", "statements", "nesStatements", "dicstatements" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    SINGLE_QUOTE=3
    DOUBLE_QUOTE=4
    COLON=5
    EQUALS=6
    SEMICOLON=7
    LINEBREAK=8
    WS=9
    STRING_SINGLE=10
    STRING_DOUBLE=11
    CODE=12
    VARIABLE=13

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
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15490) != 0):
                self.state = 16
                self.statements()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
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

        def pair(self):
            return self.getTypedRuleContext(diaParser.PairContext,0)


        def RPAREN(self):
            return self.getToken(diaParser.RPAREN, 0)

        def VARIABLE(self):
            return self.getToken(diaParser.VARIABLE, 0)

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 24
                self.match(diaParser.VARIABLE)


            self.state = 27
            self.match(diaParser.LPAREN)
            self.state = 28
            self.pair()
            self.state = 29
            self.match(diaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NesteddictionaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(diaParser.LPAREN, 0)

        def pair(self):
            return self.getTypedRuleContext(diaParser.PairContext,0)


        def RPAREN(self):
            return self.getToken(diaParser.RPAREN, 0)

        def VARIABLE(self):
            return self.getToken(diaParser.VARIABLE, 0)

        def getRuleIndex(self):
            return diaParser.RULE_nesteddictionary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNesteddictionary" ):
                listener.enterNesteddictionary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNesteddictionary" ):
                listener.exitNesteddictionary(self)




    def nesteddictionary(self):

        localctx = diaParser.NesteddictionaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nesteddictionary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 31
                self.match(diaParser.VARIABLE)


            self.state = 34
            self.match(diaParser.LPAREN)
            self.state = 35
            self.pair()
            self.state = 36
            self.match(diaParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dicstatements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diaParser.DicstatementsContext)
            else:
                return self.getTypedRuleContext(diaParser.DicstatementsContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(diaParser.COLON)
            else:
                return self.getToken(diaParser.COLON, i)

        def nesteddictionary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diaParser.NesteddictionaryContext)
            else:
                return self.getTypedRuleContext(diaParser.NesteddictionaryContext,i)


        def getRuleIndex(self):
            return diaParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)




    def pair(self):

        localctx = diaParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pair)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.dicstatements()
                self.state = 39
                self.match(diaParser.COLON)
                self.state = 42 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 42
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [10, 11, 12]:
                            self.state = 40
                            self.dicstatements()
                            pass
                        elif token in [1, 13]:
                            self.state = 41
                            self.nesteddictionary()
                            pass
                        else:
                            raise NoViableAltException(self)


                    else:
                        raise NoViableAltException(self)
                    self.state = 44 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 48 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                    break

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

        def dictionary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diaParser.DictionaryContext)
            else:
                return self.getTypedRuleContext(diaParser.DictionaryContext,i)


        def nesStatements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(diaParser.NesStatementsContext)
            else:
                return self.getTypedRuleContext(diaParser.NesStatementsContext,i)


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
        self.enterRule(localctx, 8, self.RULE_nestedStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(diaParser.LPAREN)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15490) != 0):
                self.state = 53
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 51
                    self.dictionary()
                    pass

                elif la_ == 2:
                    self.state = 52
                    self.nesStatements()
                    pass


                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
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

        def nestedStatements(self):
            return self.getTypedRuleContext(diaParser.NestedStatementsContext,0)


        def dictionary(self):
            return self.getTypedRuleContext(diaParser.DictionaryContext,0)


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
        self.enterRule(localctx, 10, self.RULE_statements)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(diaParser.CODE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(diaParser.STRING_SINGLE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.match(diaParser.STRING_DOUBLE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.nestedStatements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.dictionary()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.match(diaParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NesStatementsContext(ParserRuleContext):
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

        def nestedStatements(self):
            return self.getTypedRuleContext(diaParser.NestedStatementsContext,0)


        def SEMICOLON(self):
            return self.getToken(diaParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return diaParser.RULE_nesStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNesStatements" ):
                listener.enterNesStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNesStatements" ):
                listener.exitNesStatements(self)




    def nesStatements(self):

        localctx = diaParser.NesStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nesStatements)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(diaParser.CODE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(diaParser.STRING_SINGLE)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(diaParser.STRING_DOUBLE)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.nestedStatements()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
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


    class DicstatementsContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return diaParser.RULE_dicstatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDicstatements" ):
                listener.enterDicstatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDicstatements" ):
                listener.exitDicstatements(self)




    def dicstatements(self):

        localctx = diaParser.DicstatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dicstatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
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





