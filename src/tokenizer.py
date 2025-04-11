import re
from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str

@dataclass
class Program:
    tokens: list[Token]

# Custom exception for invalid tokens
class InvalidToken(Exception):
    def __init__(self, value):
        super().__init__(f"Unexpected token: {value}")

# def preprocess(program: str) -> str:
#     # Add spaces around special symbols so they're separate tokens
#     for ch in ['{', '}', '[', ']']:
#         program = program.replace(ch, f' {ch} ')
#     return program

# Define token regex patterns
TOKEN_PATTERNS = {
    "STRING": r'"[^"]*"',  # Matches strings enclosed in double quotes
    "NUMBER": r'-?\d+\.\d+|-?\d+',  # Matches integers and floats
    "BOOLEAN": r'\b(?:true|false)\b',  # Matches True/False
    "SYMBOL": r"'[a-zA-Z_][a-zA-Z0-9_]*", #C style identifietrs
    "KEYWORD": r'(?<!\w)(?:not|and|or|xor|get|put|print|pop|nth|dup|rot|spread|concat|stack|dec|def|inc|len|listn|list|argv|run|if|repeat|while|forever|foreach|is\-number\?|is\-list\?|is\-string\?|is\-bool\?|is\-symbol\?|sym=)(?!\w)',
    "OPERATOR": r'[+\-*/^]|=|<=|>=|!=|<|>|s=|s!=|lex<=|lex>=|lex<|lex>|b=|b!=',  # Matches operators
    "BRACKET": r'[\[\]]',  # Matches brackets
    "BRACE": r'[\{\}]',  # Matches opening and closing braces
    "IDENTIFIER": r'[a-zA-Z_][a-zA-Z0-9_]*',
    "UNKNOWN": r'\S+'  # Captures anything unexpected
    }

# Compile regex pattern to extract tokens
COMBINED_PATTERN = re.compile("|".join(f"(?P<{key}>{pattern})" for key, pattern in TOKEN_PATTERNS.items()))

def tokenize(source_code):
    tokens = []
    #source_code = preprocess(source_code)

    for match in COMBINED_PATTERN.finditer(source_code):
        token_type = match.lastgroup
        token_value = match.group()

        if token_type == "UNKNOWN":
                raise InvalidToken(token_value)  # Raise error for unexpected tokens

        tokens.append(Token(type=token_type, value=token_value))

    return tokens  # Pass tokens list to the interpreter

