from diaLexer import diaLexer
from diaParser import diaParser
from diaVisitor import diaVisitor
from antlr4 import *
import sys

class MyCustomVisitor(diaVisitor):
    def __init__(self):
        self.output = ""
        self.indent_level = 0  # Initialize the indentation level
        self.start_of_line = True  # Initialize the line start flag

    def visitNestedStatements(self, ctx: diaParser.NestedStatementsContext):
        """
        Handle the start of a block by increasing the indentation level.
        """
        self.indent_level += 1  # Increase the indentation level
        self.output = self.output.rstrip()
        self.output += ":\n"
        self.start_of_line = True  # Mark the start of a new line

        # Visit each child node in nestedStatements
        for child in ctx.getChildren():
            if isinstance(child, diaParser.NestedStatementsContext):
                continue
            self.visit(child)
        
        self.indent_level -= 1  # Decrease the indentation level after processing

    def visitStatements(self, ctx: diaParser.StatementsContext):
        indent = "    " * self.indent_level

        if ctx.CODE():
            code_segment = ctx.CODE().getText().strip()
            if ':' in code_segment:
                # Treat as a dictionary entry
                self.handleDictionary(ctx)
            else:
                # Regular code segment
                if code_segment:
                    if self.start_of_line:
                        self.output += f"{indent}{code_segment}"  # Add code segment with current indentation
                        self.start_of_line = False
                    else:
                        self.output += f"{code_segment}"
        elif ctx.STRING_SINGLE():
            string_single_segment = ctx.STRING_SINGLE().getText().strip()
            self.output += f"{string_single_segment}"
        elif ctx.STRING_DOUBLE():
            string_double_segment = ctx.STRING_DOUBLE().getText().strip()
            self.output += f"{string_double_segment}"

        # Also process children
        for child in ctx.getChildren():
            if not (child == ctx.CODE() or child == ctx.STRING_SINGLE() or child == ctx.STRING_DOUBLE()):
                self.visit(child)

        if ctx.SEMICOLON():
            self.output = self.output.rstrip(';')  # Remove ; from the output
            self.output += "\n"  # Break to new line
            self.start_of_line = True

    def handleDictionary(self, ctx):
        """
        Handle dictionary logic.
        """
        dict_entries = []
        inside_dict = False
        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                text = child.getText().strip()
                if ':' in text:
                    # Split key and value for the dictionary entry
                    key_value = text.split(':')
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].strip()
                        dict_entries.append(f"'{key}': {value}") 

        if dict_entries:
            dict_output = "{" + ", ".join(dict_entries) + "}"
            i = len(self.output)
            print(i)
            while i > -1:
                if self.output[i-1] == ':':
                    i-=1
                    break
                i-=1
            print(i)
            self.output = self.output[:i]
            self.output += f" {dict_output}"

def parse_file_with_visitor(file_path, output_file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        input_stream = InputStream(file_content)
        lexer = diaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = diaParser(token_stream)

        # Start parsing from the `rule_set` rule
        tree = parser.rule_set()

        # Create the visitor and visit the parse tree
        print('Starting parse...')
        visitor = MyCustomVisitor()
        visitor.visit(tree)
        print('Parsing completed.')

        # Write the output to a file
        with open(output_file_path, 'w') as output_file:
            output_file.write(visitor.output)
        
        print(f"Output saved to {output_file_path}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python3 parser.py {input_filename} {output_filename}')
        sys.exit(1)

    file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    parse_file_with_visitor(file_path, output_file_path)
