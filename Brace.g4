grammar Brace;

// The entry point of the grammar
rule_set : statements* EOF;

// Define tokens for curly braces
LPAREN  : '{';
RPAREN  : '}';

// Define token for CODE, which is any sequence of characters except `{`, `}`, or line breaks
CODE    : ~[{}\r\n]+;

// Define token for line breaks
LINEBREAK : [\r\n]+;

// Define token for other whitespace characters and skip them
WS      : [ \t\u000C]+ -> skip;

// Parser rules
nestedCondition : LPAREN statements* RPAREN;
statements       : CODE | nestedCondition | LINEBREAK;
