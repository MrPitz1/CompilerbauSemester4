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

// Define token for CODE, which is any sequence of characters except `{}`, line breaks, or semicolons
// Make sure CODE comes after STRING_SINGLE and STRING_DOUBLE to avoid conflict
CODE    : ~[{}\r\n'";]+;

// Define tokens for numbers and commas
NUMBER : [0-9]+;
COMMA  : ',';

// Define dictionary rule to properly recognize key-value pairs
dictionary : LPAREN key_value (COMMA key_value)* RPAREN;

// Define the key-value pairs in the dictionary
key_value : (CODE | NUMBER) ':' (CODE | NUMBER | STRING_SINGLE | STRING_DOUBLE);

// Parser rules for nested statements
nestedStatements : LPAREN statements* RPAREN;
statements       : dictionary | CODE | STRING_SINGLE | STRING_DOUBLE | nestedStatements | SEMICOLON;
