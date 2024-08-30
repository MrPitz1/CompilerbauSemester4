# Generated from C:/Users/simon/Documents/hochschule/compiler/CompilerbauSemester4/Brace.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,38,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,5,28,8,5,
        11,5,12,5,29,1,6,4,6,33,8,6,11,6,12,6,34,1,6,1,6,0,0,7,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,1,0,2,2,0,10,10,13,13,2,0,9,9,32,32,39,0,1,1,
        0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,
        0,0,13,1,0,0,0,1,15,1,0,0,0,3,18,1,0,0,0,5,20,1,0,0,0,7,22,1,0,0,
        0,9,24,1,0,0,0,11,27,1,0,0,0,13,32,1,0,0,0,15,16,5,13,0,0,16,17,
        5,10,0,0,17,2,1,0,0,0,18,19,5,13,0,0,19,4,1,0,0,0,20,21,5,10,0,0,
        21,6,1,0,0,0,22,23,5,123,0,0,23,8,1,0,0,0,24,25,5,125,0,0,25,10,
        1,0,0,0,26,28,8,0,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,
        29,30,1,0,0,0,30,12,1,0,0,0,31,33,7,1,0,0,32,31,1,0,0,0,33,34,1,
        0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,6,6,0,0,37,
        14,1,0,0,0,3,0,29,34,1,6,0,0
    ]

class BraceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    Lbrace = 4
    Rbrace = 5
    WORD = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\r\\n'", "'\\r'", "'\\n'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "Lbrace", "Rbrace", "WORD", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "Lbrace", "Rbrace", "WORD", "WS" ]

    grammarFileName = "Brace.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


