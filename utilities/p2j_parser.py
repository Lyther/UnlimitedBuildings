import re
import sys

def wrap_with_quotes(match):
    """
    Wrap the given match object with quotes.
    :param match: The match object.
    :return: The match object wrapped with quotes.
    """
    word = match.group(0)
    return f'"{word}"'

def remove_square_brackets_without_comma(match):
    """
    Remove square brackets without comma.
    :param match: The match object.
    :return: The content of the match object if it does not contain a comma, otherwise the match object itself.
    """
    content = match.group(1)
    return content if ',' not in content else match.group(0)

def remove_braces_without_colon(match):
    """
    Remove braces without colon.
    :param match: The match object.
    :return: The content of the match object if it does not contain a colon, otherwise the match object itself.
    """
    content = match.group(1)
    return content if ':' not in content else match.group(0)

def convert_to_json_style(text):
    """
    Convert the given text to JSON style (evil and dirty).
    :param text: The text to be converted.
    :return: The converted text.
    """
    # Step 1: Remove everything following a '#' (comments)
    text = re.sub(r'#[^\n]*', '', text)
    # Step 2: Replace all consecutive '\n' and '\t' with a single space ' '
    text = re.sub(r'[\n\t"]+', ' ', text)
    # Step 3: Replace '=' with ':' only if it is not followed by a number (ignoring any spaces in between)
    text = re.sub(r'=(?!\s*[\d\@])', ':', text)
    # Step 4: Remove spaces around '=', '>=', '<=', '!=', '>', '<'
    pattern = re.compile(r'([^\{\}\:\ \=\>\<\!\s]+)\s*(=|>=|<=|!=|>|<)\s*([\d\.]+|\@[^\{\}\:\ ]+)')
    text = pattern.sub(r'"\1":"\2\3"', text)
    # Step 5: Surround all continuous strings that do not contain '{', '}', ':', ' ', and not wrapped with '"' with '"'
    text = re.sub(r'[^\{\}\:\ ]+', wrap_with_quotes, text)
    text = text.replace('""', '"')
    # Step 6: Remove all spaces
    text = text.replace(' ', '')
    # Step 7: Add commas
    text = text.replace('""', '","')
    text = text.replace('}"', '},"')
    # Step 8: Add square brackets
    text = text.replace('{', '[{')
    text = text.replace('}', '}]')
    # Step 9: Remove redundant square brackets
    pattern = re.compile(r'\[([^,\[\]]+)\]')
    while pattern.search(text):
        text = re.sub(r'\[([^\[\]]+)\]', remove_square_brackets_without_comma, text)
    # Step 10: Remove redundant braces
    pattern = re.compile(r'\{([^:\{\}]+)\}')
    while pattern.search(text):
        text = re.sub(r'\{([^\{\}]+)\}', remove_braces_without_colon, text)
    # Step 11: Add braces to the first and last line
    text = '{' + text + '}'

    return text

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 p2j_parser.py <path_to_file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as file:
        mod_code = file.read()

    json_style_text = convert_to_json_style(mod_code)
    print(json_style_text)
