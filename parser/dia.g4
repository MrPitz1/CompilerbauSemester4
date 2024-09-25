grammar dia;

// The entry point of the grammar
rule_set : statements* EOF;

// Define tokens for curly braces
LPAREN  : '{';
RPAREN  : '}';

// Define tokens for end of line
SEMICOLON : ';';
LINEBREAK : [\r\n]+ -> skip;

// Define tokens for other whitespace characters and skip them
WS      : [ \t\u000C]+ -> skip;

// Define token for strings
STRING_SINGLE : '\'' (~'\'')* '\'';
STRING_DOUBLE : '"' (~'"')* '"';

// Define token for code, which is any sequence of characters except `{`, `}`, or line breaks
CODE    : ~[{}\r\n'";#]+;

// Define token for comments that start with `#` and continue to the end of the line
COMMENT_HASH : '#' (~[\r\n])* -> skip;

// Define token for single-quoted comments and skip them
COMMENT_SINGLE : '\'\'\'' (~'\'')* '\'\'\'' -> skip;

// Define token for double-quoted comments and skip them
COMMENT_DOUBLE : '"""' (~'"')* '"""' -> skip;

// Parser rules
nestedStatements : LPAREN statements* RPAREN;
statements       : CODE 
                 | STRING_SINGLE 
                 | STRING_DOUBLE 
                 | nestedStatements 
                 | SEMICOLON 
                 | COMMENT_HASH 
                 | COMMENT_SINGLE 
                 | COMMENT_DOUBLE;
