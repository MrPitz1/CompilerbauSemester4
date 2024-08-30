from pyparsing import Literal, Optional, Forward, Group, ZeroOrMore, ParseException, Word, LineEnd, printables

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
full_expr = ZeroOrMore(identifier | line_end) + Optional(nested_content('brackets')) + ZeroOrMore(identifier | line_end)

# Funktion zum Einlesen des Inhalts aus einer Datei und Parsen des Inhalts
def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        result = full_expr.parseString(file_content, parseAll=True)
        return result
    except ParseException as pe:
        return f"'{file_path}' ist ungültig: {pe}"
    except FileNotFoundError:
        return f"Datei '{file_path}' wurde nicht gefunden."

# Pfad zur Datei
file_path = 'testcode.text'

# Aufruf der Funktion und Ausgabe des Ergebnisses
parsed_result = parse_file(file_path)
print(parsed_result)
