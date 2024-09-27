from diaLexer import diaLexer
from diaParser import diaParser
from diaVisitor import diaVisitor
from antlr4 import *
import sys
import re
import os

class MyCustomVisitor(diaVisitor):
    def __init__(self):
        # Initialize output, indentation level, and line start flag
        self.output = ""
        self.indent_level = 0
        self.start_of_line = True
        self.isLambda = False

    def visitCustomDict(self, ctx: diaParser.NestedStatementsContext):
        """
        Handles custom dictionary-like structures in nested statements
        """
        for child in ctx.getChildren():
            if isinstance(child, RuleContext):
                self.output += child.getText().strip()
            elif isinstance(child, TerminalNode):
                self.output += child.getText().strip()

    def visitNestedStatements(self, ctx: diaParser.NestedStatementsContext):
        """
        Handles nested statements, adjusting indentation and calling visitCustomDict if a dictionary is detected
        """
        is_dict = False
        if self.isLambda:
            self.output += ':'
            for child in ctx.getChildren():
                self.visit(child)
            return

        # Check if any child contains a colon which might indicate a dictionary
        for child in ctx.getChildren():
            if isinstance(child, RuleContext):
                text = child.getText()
                if ':' in text and not':=' in text and not (text.startswith('{') or text.startswith('"') or text.startswith("'")):
                    is_dict = True

        # Visit custom dictionary if identified
        if is_dict:
            self.output += ' '
            self.visitCustomDict(ctx)
        
        # Handle nested statements with adjusted indentation
        else:
            self.indent_level += 1
            self.output = self.output.rstrip()
            self.output += ":\n"
            self.start_of_line = True

            # Visit all children of the current context
            for child in ctx.getChildren():
                self.visit(child)

            self.indent_level -= 1

    def visitStatements(self, ctx: diaParser.StatementsContext):
        """
        Handles different types of statements, including CODE, STRING_SINGLE, and STRING_DOUBLE.
        """
        indent = "    " * self.indent_level
        self.isLambda = False
        if ctx.CODE():
            code_text = ctx.CODE().getText().strip()
            if "lambda" in code_text:
                self.isLambda = True
            if code_text:
                if self.start_of_line:
                    self.output += f"{indent}{code_text}"
                    self.start_of_line = False
                else:
                    self.output += f"{code_text}"
        elif ctx.STRING_SINGLE():
            string_single_text = ctx.STRING_SINGLE().getText().strip()
            self.output += f"{string_single_text}"
        elif ctx.STRING_DOUBLE():
            string_double_text = ctx.STRING_DOUBLE().getText().strip()
            self.output += f"{string_double_text}"

        # Process children nodes
        for child in ctx.getChildren():
            if not (child == ctx.CODE() or child == ctx.STRING_SINGLE() or child == ctx.STRING_DOUBLE()):
                self.visit(child)

        if ctx.SEMICOLON():
            self.output += "\n"  # Add newline
            self.start_of_line = True

def parse_file_with_visitor(input_file_path, output_file_path):
    """
    Parse the input file using the custom visitor and save the output to a file.
    """
    try:
        # Read input file
        with open(input_file_path, 'r') as file:
            file_content = file.read()

        # Set up the lexer, parser, and parse tree
        input_stream = InputStream(file_content)
        lexer = diaLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = diaParser(token_stream)
        tree = parser.rule_set()  # Start parsing from the rule_set rule
        print('Starting parse...')

        # Create and use the visitor
        visitor = MyCustomVisitor()
        visitor.visit(tree)

        print('Parsing completed.')

        # Save the output to a file
        with open(output_file_path, 'w') as output_file:
            output_file.write(visitor.output)
        
        print(f"Output saved to {output_file_path}")
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python3 parser.py {input_filename} {output_filename}')
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    parse_file_with_visitor(input_file_path, output_file_path)
