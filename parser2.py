from pyparsing import Literal, Forward, Group, ZeroOrMore, ParseException, Word, OneOrMore, printables, LineEnd

# Definition der Tokens
Lbrace = Literal('{').suppress()
Rbrace = Literal('}').suppress()

# Zeilenumbrüche als spezielles Token behandeln
line_end = LineEnd().setParseAction(lambda t: 'line_end')

# Alles außer {, }, und line_end als 'word' und formatiert als 'word: inhalt'
identifier = Word(printables, excludeChars='{}').setParseAction(lambda t: f'word: {t[0]}')

# Definition für den Inhalt innerhalb der geschweiften Klammern
nested_content = Forward()
nested_content <<= Group(Lbrace + ZeroOrMore(identifier | nested_content | line_end) + Rbrace)

# Definition für den gesamten Ausdruck, der auch Bezeichner außerhalb der geschweiften Klammern erkennt
full_expr = ZeroOrMore(identifier | line_end) + nested_content('brackets') + ZeroOrMore(identifier | line_end)

# Beispiel-Eingaben
test_strings = [
    """
def factorial(n)
{
   if n == 0
   { 
    return 1;
   }
   else
   {
       return n * factorial(n-1);
   }
}
number = 5;
# Berechnung der Fakultaet
result = factorial(number);

    """,
]

for test in test_strings:
    try:
        result = full_expr.parseString(test, parseAll=True)
        print(result)
    except ParseException as pe:
        print(f"'{test}' ist ungültig: {pe}")
