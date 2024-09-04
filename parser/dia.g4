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

DICTIONARY : '{' (KEY ':' VALUE (',' KEY ':' VALUE)*)? '}';

fragment KEY : [a-zA-Z0-9_]+           // Unquoted key
             | '\'' [a-zA-Z0-9_]+ '\''  // Single-quoted key
             | '"' [a-zA-Z0-9_]+ '"'  // Double-quoted key
             ;

fragment VALUE : '\'' (~['\\'] | '\\' . )* '\''  // Single-quoted string value
               | '"' (~['\\'] | '\\' . )* '"'   // Double-quoted string value
               | 'True'                         // Boolean True
               | 'False'                        // Boolean False
               | [a-zA-Z0-9_]+                  // Unquoted value (like a variable name)
               | NUMBER                         // Numeric value
               | '{' (KEY ':' VALUE (',' KEY ':' VALUE)*)? '}'
               ;

// Fragment for numbers (integers and floats)
fragment NUMBER : [0-9]+ ('.' [0-9]+)?;

// Define token for CODE, which is any sequence of characters except `{`, `}`, or line breaks
// Make sure CODE comes after STRING_SINGLE and STRING_DOUBLE to avoid conflict
CODE    : ~[{}\r\n'";]+;

// Parser rules
nestedStatements : LPAREN statements* RPAREN;
statements       : CODE | STRING_SINGLE | STRING_DOUBLE | DICTIONARY | nestedStatements | SEMICOLON;
