grammar dia;

// The entry point of the grammar
rule_set : statements* EOF;


// Define tokens to skip comments
COMMENT_HASH : '#' ~[\r\n]* -> skip;
COMMENT_SINGLE : '\'\'\'' (~'\'')* '\'\'\'' -> skip;
COMMENT_DOUBLE : '"""' (~'"')* '"""' -> skip;

// Define tokens for curly braces
LPAREN      : '{';
RPAREN      : '}';

// Define tokens for end of line
SEMICOLON   : ';';
LINEBREAK    : [\r\n]+ -> skip;

// Define tokens for other whitespace characters and skip them
WS           : [ \t\u000C]+ -> skip;

// Define tokens for strings
STRING_SINGLE : '\'' (~'\'')* '\'';
STRING_DOUBLE : '"' (~'"')* '"';

// Define token for code, which is any sequence of characters except `{`, `}`, or line breaks
CODE         : ~[{}\r\n'";#]+;

// Parser rules
nestedStatements : LPAREN statements* RPAREN;

// Statements
statements       : CODE 
                 | STRING_SINGLE 
                 | STRING_DOUBLE 
                 | nestedStatements 
                 | SEMICOLON 
                 | COMMENT_HASH 
                 | COMMENT_SINGLE 
                 | COMMENT_DOUBLE;