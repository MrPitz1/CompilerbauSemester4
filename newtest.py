from antlr4 import *
from BraceLexer import BraceLexer
from BraceParser import BraceParser
from antlr4.error.ErrorListener import ErrorListener
import json

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Line {line}:{column} {msg}")

def parse_tree_to_list(node):
    """
    Convert an ANTLR parse tree node into a nested list format, including line_end.
    """
    if isinstance(node, TerminalNode):
        # Handle terminal nodes (tokens)
        token_type = node.symbol.type
        token_text = node.getText().strip()
        # Special handling for line_end (newline) tokens

        return {token_type: token_text} 
    
    if isinstance(node, ParserRuleContext):
        # Handle parser rule contexts (nodes)
        result = []
        for child in node.getChildren():
            child_list = parse_tree_to_list(child)
            if child_list is not None:  # Only add non-empty lists
                result.append(child_list)
        # Create a dictionary for the current rule context if it has children
        if result:
            rule_name = node.__class__.__name__.replace("Context", "")
            return {rule_name: result}
        return None

def nested_list_to_json(nested_list):
    """
    Convert a nested list representation to a JSON-compatible dictionary.
    """
    def convert_to_json(obj):
        if isinstance(obj, dict):
            return {k: convert_to_json(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_json(i) for i in obj]
        else:
            return obj

    return convert_to_json(nested_list)

def parse_file(file_path):
    """
    Parse the file and convert the parse tree to a JSON representation.
    """
    error_listener = CustomErrorListener()
    
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        input_stream = InputStream(file_content)
        lexer = BraceLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = BraceParser(token_stream)

        # Attach the custom error listener to the parser
        parser.addErrorListener(error_listener)

        # Start parsing from the 'rule_set' rule
        tree = parser.rule_set()

        # Check if there were any syntax errors
        if error_listener.errors:
            return f"Errors during parsing: {'; '.join(error_listener.errors)}"
        
        # Convert the parse tree to a nested list representation
        tree_list = parse_tree_to_list(tree)

        # Convert the nested list to a JSON-compatible dictionary
        if tree_list:
            json_data = nested_list_to_json(tree_list)
            json_str = json.dumps(json_data, indent=2)
            return json_str
        return "No content to convert."
    except FileNotFoundError:
        return f"Datei '{file_path}' wurde nicht gefunden."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Pfad zur Datei
file_path = 'testcode.text'

# Parse the file and get the JSON representation of the parse tree
json_str = parse_file(file_path)
print("JSON Output:")
print(json_str)
