#Command: pytest test.py -v
import pytest
from src.Interpreter import *

@pytest.mark.parametrize("source, expected", [
    ("""2 3 -""", ""),
    ("""2 dec print""", "1"),
    ("""2 3 - print""", "-1"),
    ("10 2 / put", "5.0"),
    ('true false and put', "false"),
    ('45 44 > 45 45 < or put', "true"),
    ('[  ]', ""),
    ( " [ 1 2 3 ]", ""),
    ( "[ 1 2 1 2 ]", ""),
    ( '[ 1 2 3 4 5 6 pop pop pop ]', ""),
    ( '[ 1 2 [ 3 4 ] ]', ""),
    ( '2 3 + put', "5"),
    ( '[ 1 2 3 ] 2 nth put', "3"),
    ( '[ 1 2 [ 3 4 ] ] 2 nth 0 nth put', "3"),
    ( '[ 1 2 3 ] spread * + put', "7"),
    ( '2 3 >= put ', "false"),
    ( 'true false b= put', "false"),
    ( '"abc" "abc" lex>= put', "true"),
    ( '"abc" "abcd" lex< put', "true"),
    ("""[1 2 3 4] len print""", "4"),
    ("""[1 2 3 4] print""", "[1, 2, 3, 4]"),
    ("""1 2 3 4 2 listn print""", "[3, 4]"),
    ("""1 2 3 4 list print""", "[1, 2, 3, 4]"),
    ("""[1 2 3 4] print""", "[1, 2, 3, 4]"),
    ("1 print", "1"),
    ("""list print""", "[]"),
    ("""{"Hello" print}""", "" ),
    ("""{"Hello" print} run""", "Hello" ),
    ("""5 0 > { "Positive" print }{ "Not positive" print } if """, "Positive"),
    ("""-1 0 > { "Positive" print }{ "Not positive" print } if """, "Not positive"),
    ("""10 { "." print } repeat""", ".\n.\n.\n.\n.\n.\n.\n.\n.\n."),
    ("5 { dup 0 > } { dup print dec } while", "5\n4\n3\n2\n1"),
    ("5 { dup 0 > } { dup print dec } while print", "5\n4\n3\n2\n1\n0"),


])
def test_eval(capsys, source, expected):
    forth_interpreter(source)
    captured = capsys.readouterr()

    assert captured.out.strip() == expected


def test_single_case(capsys):
    source = "1 2 3 4 list print"
    expected = "[1, 2, 3, 4]"
    
    forth_interpreter(source)
    captured = capsys.readouterr()
    
    print("Captured Output:", repr(captured.out.strip()))  # Debugging output
    assert captured.out.strip() == expected