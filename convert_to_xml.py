from xml.etree.ElementTree import Element, tostring
import xml.dom.minidom

# Define a class for Instructions
class Instruction:
    def __init__(self, text):
        self.text = text

    def to_xml(self):
        instruction = Element('Instruction')
        instruction.text = self.text
        return instruction

# Define a class for Blocks
class Block:
    def __init__(self):
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def to_xml(self):
        block_elem = Element('Block')
        for instr in self.instructions:
            if isinstance(instr, Instruction):
                block_elem.append(instr.to_xml())
            elif isinstance(instr, Element):
                block_elem.append(instr)
        return block_elem

# Convert BrackPy code to XML
def brackpy_code_to_xml(brackpy_code: str) -> str:
    lines = brackpy_code.splitlines()
    root = Element('Root')
    stack = [Block()]  # Stack for blocks, starting with the Root block

    def handle_line(line):
        # Remove leading and trailing whitespace
        line = line.strip()

        # Skip empty lines or comments
        if not line or line.startswith('#'):
            return

        # Handle block start and end
        if line.endswith('{'):
            current_block = Block()
            stack[-1].add_instruction(Instruction(line.rstrip('{')))
            stack.append(current_block)
        elif line.endswith('}'):
            finished_block = stack.pop()
            if stack:
                stack[-1].add_instruction(finished_block.to_xml())
        else:
            # Remove semicolons from the end of the line and add as an instruction
            stack[-1].add_instruction(Instruction(line.rstrip(';')))

    for line in lines:
        handle_line(line)

    # If there is still a block remaining, add it
    if len(stack) == 1:
        root.append(stack[0].to_xml())

    # Format and convert to string
    xml_str = tostring(root, 'utf-8')
    parsed_xml = xml.dom.minidom.parseString(xml_str)
    return parsed_xml.toprettyxml(indent='  ')

# Main part of the script
if __name__ == '__main__':
    # Read BrackPy code from the file
    with open('sample_code.bpy', 'r') as file:
        brackpy_code = file.read()

    # Convert the code to XML
    xml_content = brackpy_code_to_xml(brackpy_code)

    # Save the XML output to a file
    with open('output_code.xml', 'w') as file:
        file.write(xml_content)

    print("BrackPy code has been successfully converted to XML and saved in 'output_code.xml'.")
