import re
import sys

def convert_to_mod_style(text):
    """
    Convert the given json text to mod style (evil and dirty).
    :param text: The text to be converted.
    :return: The converted text.
    """
    # Step 1: Remove braces from the first and last line
    text = text[1:-1]
    # Step 2: Remove square brackets
    text = text.replace('[', ' ')
    text = text.replace(']', ' ')
    # Step 3: Replace quotes with spaces
    text = text.replace('"', ' ')
    # Step 4: Replace colons with equal signs
    text = text.replace(':', ' = ')
    # Step 5: New line after each open brace, before and after each close brace, and replace comma
    text = text.replace('{', ' {\n')
    text = text.replace('}', '\n}\n')
    text = text.replace(',', '\n')
    # Step 6: Remove redundant conditions
    text = re.sub(r'=\s*=', ' = ', text)
    text = re.sub(r'=\s*<', ' < ', text)
    text = re.sub(r'=\s*>', ' > ', text)
    text = re.sub(r'=\s*<=', ' <= ', text)
    text = re.sub(r'=\s*>=', ' >= ', text)
    text = re.sub(r'=\s*!=', ' != ', text)
    # Step 7: Remove redundant spaces
    text = re.sub(r'[ ]+', ' ', text)
    # Step 8: Remove empty lines
    text = re.sub(r'\n[ ]*\n', '\n', text)
    # Step 9: Remove beginning and ending spaces for each line
    text = text.strip()
    text = re.sub(r'\n[ ]+', '\n', text)
    text = re.sub(r'[ ]+\n', '\n', text)

    return text

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 j2p_parser.py <path_to_file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as file:
        json_code = file.read()

    mod_style_text = convert_to_mod_style(json_code)
    print(mod_style_text)
