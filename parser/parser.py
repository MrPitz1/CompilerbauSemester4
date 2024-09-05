from diaLexer import diaLexer
from diaParser import diaParser
from diaVisitor import diaVisitor
from antlr4 import *
import sys
import re

class MyCustomVisitor(diaVisitor):
    def __init__(self):
        self.output = ""
        self.indent_level = 0  # Initialize the indentation level
        self.start_of_line = True  # Initialize the line start flag
    def visitCustomDict(self, ctx: diaParser.NestedStatementsContext):
        for child in ctx.getChildren():
            if isinstance(child, RuleContext):
                self.output += child.getText().strip()
            if isinstance(child, TerminalNode):
                self.output += child.getText().strip()
    def visitNestedStatements(self, ctx: diaParser.NestedStatementsContext):
        """
        Handle the start of a block by increasing the indentation level.
        """
        is_dict = False
        skip = False
        for i, child in enumerate(ctx.getChildren()):
            if isinstance(child, RuleContext):
                if ':' in child.getText() and child.getText()[0] != '{':
                    is_dict = True
        if is_dict:
            self.visitCustomDict(ctx)   
        else:
            self.indent_level += 1  # Increase the indentation level
            self.output = self.output.rstrip()
            self.output += ":\n"
            self.start_of_line = True  # Mark the start of a new line
            for child in ctx.getChildren():
                self.visit(child)
            self.indent_level -= 1  # Decrease the indentation level after processing
    
    def visitStatements(self, ctx: diaParser.StatementsContext):
        indent = "    " * self.indent_level

        if ctx.CODE():
            code_segment = ctx.CODE().getText().strip()
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
        print(tree.toStringTree(recog=parser))
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
