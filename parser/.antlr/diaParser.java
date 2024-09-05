// Generated from c:/Users/simon/Documents/hochschule/compiler/CompilerbauSemester4/parser/dia.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class diaParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LPAREN=1, RPAREN=2, SEMICOLON=3, LINEBREAK=4, WS=5, STRING_SINGLE=6, STRING_DOUBLE=7, 
		CODE=8;
	public static final int
		RULE_rule_set = 0, RULE_nestedStatements = 1, RULE_statements = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"rule_set", "nestedStatements", "statements"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LPAREN", "RPAREN", "SEMICOLON", "LINEBREAK", "WS", "STRING_SINGLE", 
			"STRING_DOUBLE", "CODE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "dia.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public diaParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Rule_setContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(diaParser.EOF, 0); }
		public List<StatementsContext> statements() {
			return getRuleContexts(StatementsContext.class);
		}
		public StatementsContext statements(int i) {
			return getRuleContext(StatementsContext.class,i);
		}
		public Rule_setContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rule_set; }
	}

	public final Rule_setContext rule_set() throws RecognitionException {
		Rule_setContext _localctx = new Rule_setContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_rule_set);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 458L) != 0)) {
				{
				{
				setState(6);
				statements();
				}
				}
				setState(11);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(12);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NestedStatementsContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(diaParser.LPAREN, 0); }
		public TerminalNode RPAREN() { return getToken(diaParser.RPAREN, 0); }
		public List<StatementsContext> statements() {
			return getRuleContexts(StatementsContext.class);
		}
		public StatementsContext statements(int i) {
			return getRuleContext(StatementsContext.class,i);
		}
		public NestedStatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nestedStatements; }
	}

	public final NestedStatementsContext nestedStatements() throws RecognitionException {
		NestedStatementsContext _localctx = new NestedStatementsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_nestedStatements);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			match(LPAREN);
			setState(18);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 458L) != 0)) {
				{
				{
				setState(15);
				statements();
				}
				}
				setState(20);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(21);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementsContext extends ParserRuleContext {
		public TerminalNode CODE() { return getToken(diaParser.CODE, 0); }
		public TerminalNode STRING_SINGLE() { return getToken(diaParser.STRING_SINGLE, 0); }
		public TerminalNode STRING_DOUBLE() { return getToken(diaParser.STRING_DOUBLE, 0); }
		public NestedStatementsContext nestedStatements() {
			return getRuleContext(NestedStatementsContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(diaParser.SEMICOLON, 0); }
		public StatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statements; }
	}

	public final StatementsContext statements() throws RecognitionException {
		StatementsContext _localctx = new StatementsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statements);
		try {
			setState(28);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CODE:
				enterOuterAlt(_localctx, 1);
				{
				setState(23);
				match(CODE);
				}
				break;
			case STRING_SINGLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				match(STRING_SINGLE);
				}
				break;
			case STRING_DOUBLE:
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				match(STRING_DOUBLE);
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 4);
				{
				setState(26);
				nestedStatements();
				}
				break;
			case SEMICOLON:
				enterOuterAlt(_localctx, 5);
				{
				setState(27);
				match(SEMICOLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\b\u001f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0005\u0000\b\b\u0000\n\u0000\f\u0000\u000b"+
		"\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0005\u0001\u0011"+
		"\b\u0001\n\u0001\f\u0001\u0014\t\u0001\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002\u001d\b\u0002"+
		"\u0001\u0002\u0000\u0000\u0003\u0000\u0002\u0004\u0000\u0000!\u0000\t"+
		"\u0001\u0000\u0000\u0000\u0002\u000e\u0001\u0000\u0000\u0000\u0004\u001c"+
		"\u0001\u0000\u0000\u0000\u0006\b\u0003\u0004\u0002\u0000\u0007\u0006\u0001"+
		"\u0000\u0000\u0000\b\u000b\u0001\u0000\u0000\u0000\t\u0007\u0001\u0000"+
		"\u0000\u0000\t\n\u0001\u0000\u0000\u0000\n\f\u0001\u0000\u0000\u0000\u000b"+
		"\t\u0001\u0000\u0000\u0000\f\r\u0005\u0000\u0000\u0001\r\u0001\u0001\u0000"+
		"\u0000\u0000\u000e\u0012\u0005\u0001\u0000\u0000\u000f\u0011\u0003\u0004"+
		"\u0002\u0000\u0010\u000f\u0001\u0000\u0000\u0000\u0011\u0014\u0001\u0000"+
		"\u0000\u0000\u0012\u0010\u0001\u0000\u0000\u0000\u0012\u0013\u0001\u0000"+
		"\u0000\u0000\u0013\u0015\u0001\u0000\u0000\u0000\u0014\u0012\u0001\u0000"+
		"\u0000\u0000\u0015\u0016\u0005\u0002\u0000\u0000\u0016\u0003\u0001\u0000"+
		"\u0000\u0000\u0017\u001d\u0005\b\u0000\u0000\u0018\u001d\u0005\u0006\u0000"+
		"\u0000\u0019\u001d\u0005\u0007\u0000\u0000\u001a\u001d\u0003\u0002\u0001"+
		"\u0000\u001b\u001d\u0005\u0003\u0000\u0000\u001c\u0017\u0001\u0000\u0000"+
		"\u0000\u001c\u0018\u0001\u0000\u0000\u0000\u001c\u0019\u0001\u0000\u0000"+
		"\u0000\u001c\u001a\u0001\u0000\u0000\u0000\u001c\u001b\u0001\u0000\u0000"+
		"\u0000\u001d\u0005\u0001\u0000\u0000\u0000\u0003\t\u0012\u001c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}