grammar dia;

// The entry point of the grammar
rule_set : statements* EOF;

// Define tokens for curly braces
LPAREN  : '{';
RPAREN  : '}';

// Define tokens for quotes
SINGLE_QUOTE : '\'';
DOUBLE_QUOTE : '"';

// Define tokens for colon (used in key-value pairs in dictionaries)
Walros : ':=';
COLON : ':';
EQUALS : '=';
COMMA : ',';
DOLLAR : '$';

// Define tokens for end of line (semicolon is used to identify line breaks)
SEMICOLON : ';';
LINEBREAK : [\r\n]+ -> skip;

// Define tokens for other whitespace characters and skip them
WS      : [ \t\u000C]+ -> skip;

// Define token for strings
STRING_SINGLE : '\'' (~'\'')* '\'';
STRING_DOUBLE : '"' (~'"')* '"';

// Define token for CODE, which is any sequence of characters except `{`, `}`, `:`, or line breaks
// Make sure CODE comes after STRING_SINGLE and STRING_DOUBLE to avoid conflict
CODE    : ~[{}\r\n,$:;'"]+;

// Parser rules
dictionary       : (VARIABLE)? LPAREN pair RPAREN;  // Handle multiple pairs inside the dictionary
nesteddictionary : (VARIABLE)? LPAREN pair RPAREN;
pair             : (dicstatements COLON (dicstatements| nesteddictionary)+)+;
VARIABLE         : CODE* EQUALS;

nestedStatements : LPAREN (dictionary | nesStatements)* RPAREN;

// Main statements rule (no standalone colons allowed)
statements       : CODE 
                 | STRING_SINGLE 
                 | STRING_DOUBLE 
                 | nestedStatements
                 | dictionary
                 | SEMICOLON
                 | COMMA
                 | DOLLAR;

nesStatements    : CODE 
                 | STRING_SINGLE 
                 | STRING_DOUBLE 
                 | nestedStatements
                 | SEMICOLON
                 | COMMA
                 | DOLLAR;

dicstatements    : CODE | STRING_SINGLE | STRING_DOUBLE | COMMA;
