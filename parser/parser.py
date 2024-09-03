from diaLexer import diaLexer
from diaParser import diaParser
from diaListener import diaListener
from antlr4 import *
import sys

class MyCustomListener(diaListener):
    def __init__(self):
        self.output = ""
        self.indent_level = 0  # Initialize the indentation level

    def enterNestedStatements(self, ctx):
        """
        Handle the start of a block by increasing the indentation level.
        """
        self.indent_level += 1  # Increase the indentation level
        self.output += ':'
    def exitNestedStatements(self, ctx):
        self.indent_level -= 1  # Decrease the indentation level

    def enterStatements(self, ctx):
        indent = "    " * self.indent_level
        if ctx.CODE():
            code_segment = ctx.CODE().getText().strip()
            if code_segment:
                self.output += f"{indent}{code_segment}"  # Add code segment with current indentation
        elif ctx.STRING_SINGLE():
            string_single_segment = ctx.STRING_SINGLE().getText().strip()
            if string_single_segment:
                self.output += f"{string_single_segment}"
        elif ctx.STRING_DOUBLE():
            string_double_segment = ctx.STRING_DOUBLE().getText().strip()
            if string_double_segment:
                self.output += f"{string_double_segment}"
        elif ctx.LINEBREAK():
            self.output += "\n"  # Add a line break

def parse_file_with_listener(file_path, output_file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        input_stream = InputStream(file_content)
        lexer = diaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = diaParser(token_stream)

        # Start parsing from the `rule_set` rule
        tree = parser.rule_set()

        # Create the listener and walk through the parse tree
        listener = MyCustomListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Write the output to a file
        with open(output_file_path, 'w') as output_file:
            output_file.write(listener.output)
        
        print(f"Output saved to {output_file_path}")
    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
        output_file_path = sys.argv[2]  # The second argument is the output file path
    except:
        print('Usage: python3 parser.py {input_filename} {output_filename}')
        sys.exit(0)
    parse_file_with_listener(file_path, output_file_path)
