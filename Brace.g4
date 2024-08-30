grammar Brace;

// Einstiegspunkt
expression : (identifier | line_end)* nested_content? (identifier | line_end)* ;

// Regel für geschachtelten Inhalt innerhalb von geschweiften Klammern
nested_content : Lbrace (identifier | nested_content | line_end)* Rbrace ;

// Regel für Bezeichner (identifiers)
identifier : WORD ;

// Regel für Zeilenumbrüche
line_end : '\r\n' | '\r' | '\n' ;

// Regel für geschweifte Klammern
Lbrace : '{' ;
Rbrace : '}' ;

// Regel für Wörter (identifier) - erlaubt alles außer { und }
WORD : ~[\r\n]+ ;

// Regel für Whitespace-Zeichen (werden übersprungen)
WS : [ \t]+ -> skip ;