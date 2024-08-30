from antlr4 import *
from BraceLexer import BraceLexer
from BraceParser import BraceParser

def parse_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        input_stream = InputStream(file_content)
        lexer = BraceLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = BraceParser(token_stream)
        tree = parser.expression()

        return tree.toStringTree(recog=parser)
    except FileNotFoundError:
        return f"Datei '{file_path}' wurde nicht gefunden."

# Pfad zur Datei
file_path = 'testcode.text'

x = parse_file(file_path)
print(x)