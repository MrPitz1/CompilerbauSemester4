grammar dia;

// The entry point of the grammar
rule_set : statements* EOF;

// Define tokens for curly braces
LPAREN  : '{';
RPAREN  : '}';

// Define tokens for quotes
SINGLE_QUOTE : '\'';
DOUBLE_QUOTE : '"';

// Define tokens for line breaks
LINEBREAK : [\r\n]+;

// Define tokens for other whitespace characters and skip them
WS      : [ \t\u000C]+ -> skip;

// Define token for strings
STRING_SINGLE : '\'' (~'\'')* '\'';
STRING_DOUBLE : '"' (~'"')* '"';

// Define token for CODE, which is any sequence of characters except `{`, `}`, or line breaks
// We need to make sure CODE comes after STRING_SINGLE and STRING_DOUBLE to avoid conflict
CODE    : ~[{}\r\n'"]+;

// Parser rules
nestedStatements : LPAREN statements* RPAREN;
statements       : CODE | STRING_SINGLE | STRING_DOUBLE | nestedStatements | LINEBREAK;
