grammar dia;

// The entry point of the grammar
rule_set : statements* EOF;

// Define tokens for curly braces
LPAREN  : '{';
RPAREN  : '}';

// Define tokens for quotes
SINGLE_QUOTE : '\'';
DOUBLE_QUOTE : '"';

// Define tokens for end of line
SEMICOLON : ';';
LINEBREAK : [\r\n]+ -> skip;

// Define tokens for other whitespace characters and skip them
WS      : [ \t\u000C]+ -> skip;

// Define token for strings
STRING_SINGLE : '\'' (~'\'')* '\'';
STRING_DOUBLE : '"' (~'"')* '"';

// Define token for CODE, which is any sequence of characters except `{`, `}`, or line breaks
// Make sure CODE comes after STRING_SINGLE and STRING_DOUBLE to avoid conflict
CODE    : ~[{}\r\n'";]+;

// Add a rule for dictionary parsing
dictionary : LPAREN (key_value (',' key_value)*)? RPAREN;

key_value : CODE ':' (CODE | STRING_SINGLE | STRING_DOUBLE);

// Parser rules
nestedStatements : LPAREN statements* RPAREN;
statements       : CODE | STRING_SINGLE | STRING_DOUBLE | nestedStatements | dictionary | SEMICOLON;
