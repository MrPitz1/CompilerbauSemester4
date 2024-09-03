# Generated from ./dia.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,62,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,4,4,29,
        8,4,11,4,12,4,30,1,5,4,5,34,8,5,11,5,12,5,35,1,5,1,5,1,6,1,6,5,6,
        42,8,6,10,6,12,6,45,9,6,1,6,1,6,1,7,1,7,5,7,51,8,7,10,7,12,7,54,
        9,7,1,7,1,7,1,8,4,8,59,8,8,11,8,12,8,60,0,0,9,1,1,3,2,5,3,7,4,9,
        5,11,6,13,7,15,8,17,9,1,0,5,2,0,10,10,13,13,3,0,9,9,12,12,32,32,
        1,0,39,39,1,0,34,34,6,0,10,10,13,13,34,34,39,39,123,123,125,125,
        66,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,
        21,1,0,0,0,5,23,1,0,0,0,7,25,1,0,0,0,9,28,1,0,0,0,11,33,1,0,0,0,
        13,39,1,0,0,0,15,48,1,0,0,0,17,58,1,0,0,0,19,20,5,123,0,0,20,2,1,
        0,0,0,21,22,5,125,0,0,22,4,1,0,0,0,23,24,5,39,0,0,24,6,1,0,0,0,25,
        26,5,34,0,0,26,8,1,0,0,0,27,29,7,0,0,0,28,27,1,0,0,0,29,30,1,0,0,
        0,30,28,1,0,0,0,30,31,1,0,0,0,31,10,1,0,0,0,32,34,7,1,0,0,33,32,
        1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,
        37,38,6,5,0,0,38,12,1,0,0,0,39,43,5,39,0,0,40,42,8,2,0,0,41,40,1,
        0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,
        43,1,0,0,0,46,47,5,39,0,0,47,14,1,0,0,0,48,52,5,34,0,0,49,51,8,3,
        0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,
        1,0,0,0,54,52,1,0,0,0,55,56,5,34,0,0,56,16,1,0,0,0,57,59,8,4,0,0,
        58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,18,1,
        0,0,0,6,0,30,35,43,52,60,1,6,0,0
    ]

class diaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LPAREN = 1
    RPAREN = 2
    SINGLE_QUOTE = 3
    DOUBLE_QUOTE = 4
    LINEBREAK = 5
    WS = 6
    STRING_SINGLE = 7
    STRING_DOUBLE = 8
    CODE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'''", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "SINGLE_QUOTE", "DOUBLE_QUOTE", "LINEBREAK", 
            "WS", "STRING_SINGLE", "STRING_DOUBLE", "CODE" ]

    ruleNames = [ "LPAREN", "RPAREN", "SINGLE_QUOTE", "DOUBLE_QUOTE", "LINEBREAK", 
                  "WS", "STRING_SINGLE", "STRING_DOUBLE", "CODE" ]

    grammarFileName = "dia.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

