grammar Brace;

// The entry point of the grammar
rule_set : statements* EOF;

// Define tokens for curly braces
LPAREN  : '{';
RPAREN  : '}';

// Define tokens for quotes
SINGLE_QUOTE : '\'';
DOUBLE_QUOTE : '"';

// Define token for CODE, which is any sequence of characters except `{`, `}`, or line breaks
CODE    : ~[{}\r\n]+;

// Define tokens for strings
STRING_SINGLE : '\'' (~'\'')* '\'' ;
STRING_DOUBLE : '"' (~'"')* '"' ;

// Define token for line breaks
LINEBREAK : [\r\n]+;

// Define token for other whitespace characters and skip them
WS      : [ \t\u000C]+ -> skip;

// Parser rules
nestedCondition : LPAREN statements* RPAREN;
statements       : CODE | STRING_SINGLE | STRING_DOUBLE | nestedCondition | LINEBREAK;
