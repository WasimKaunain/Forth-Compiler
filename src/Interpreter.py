from src.tokenizer import *
from more_itertools import peekable

def forth_interpreter(program):
    stack = []
    tokens = tokenize(program)  # Extract tokens correctly

    def get_input():
        value = input()
        try:
            return float(value) if '.' in value else int(value)
        except ValueError:
            return value  # Keep it as a string if not a number
            
    def is_number(value):
        return isinstance(value, (int, float))

    def Operation(token, A = None):
        match token:
            case '+': 
                if is_number(stack[-1]) and is_number(stack[-2]) and A is None:
                    stack.append(stack.pop(-2) + stack.pop())
                elif A is not None:
                    A.append(A.pop(-2) + A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Cannot add string and number")
                else:
                    exit("Error: Cannot add string and number")

            case '-':
                if is_number(stack[-1]) and is_number(stack[-2]) and A is None:
                    stack.append(stack.pop(-2) - stack.pop()) 
                elif A is not None:
                    A.append(A.pop(-2) - A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Cannot subtract string and number")
                else: 
                    exit("Error: Cannot subtract string and number")

            case'*': 
                if is_number(stack[-1]) and is_number(stack[-2]) and A is None:
                    stack.append(stack.pop(-2) * stack.pop()) 
                elif A is not None:
                    A.append(A.pop(-2) * A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Cannot multiply string and number")
                else:
                    exit("Error: Cannot multiply string and number")

            case '/':
                if is_number(stack[-1]) and is_number(stack[-2]) and A is None:
                    stack.append(stack.pop(-2) / stack.pop()) 
                elif A is not None:
                    A.append(A.pop(-2) / A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Cannot divide string and number")
                else:
                    exit("Error: Cannot divide string and number")

            case '^':
                if is_number(stack[-1]) and is_number(stack[-2]) and A is None:
                    stack.append(stack.pop(-2) ** stack.pop()) 
                elif A is not None:
                    A.append(A.pop(-2) ** A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Cannot exponentiate string and number")
                else:
                    exit("Error: Cannot exponentiate string and number")

            case 'not':
                if stack[-1] in [True, False] and A is None:
                    stack.append(not stack.pop()) 
                elif A is not None:
                    A.append(not A.pop()) if A[-1] in [True, False] else exit("Error: Cannot negate non-boolean")
                else:
                    exit("Error: Cannot negate non-boolean")

            case 'and':
                if stack[-1] in [True, False] and stack[-2] in [True, False] and A is None:
                    stack.append(stack.pop(-2) and stack.pop()) 
                elif A is not None:
                    A.append(A.pop(-2) and A.pop()) if stack[-1] in [True, False,0,1] and stack[-2] in [True, False,0,1] else exit("Error: Cannot perform AND operation on non-boolean")
                else:
                    exit("Error: Cannot perform AND operation on non-boolean")

            case 'or':
                if stack[-1] in [True, False] and stack[-2] in [True, False] and A is None:
                    stack.append(stack.pop(-2) or stack.pop()) 
                elif A is not None:
                    A.append(A.pop(-2) or A.pop()) if stack[-1] in [True, False,0,1] and stack[-2] in [True, False,0,1] else exit("Error: Cannot perform OR operation on non-boolean")
                else:
                    exit("Error: Cannot perform OR operation on non-boolean")

            case 'xor':
                if stack[-1] in [True, False] and stack[-2] in [True, False] and A is None:
                    stack.append(stack.pop(-2) ^ stack.pop()) 
                elif A is not None:
                    A.append(A.pop(-2) ^ A.pop()) if stack[-1] in [True, False,0,1] and stack[-2] in [True, False,0,1] else exit("Error: Cannot perform XOR operation on non-boolean")

                else:
                    exit("Error: Cannot perform XOR operation on non-boolean")

            case 'get':
                if A is None:
                    stack.append(get_input())
                else:
                    A.append(get_input())

            case 'put':
                if A is None:
                    print(stack.pop() if stack[-1] not in [True,False] else str(stack.pop()).lower()) if len(stack) > 0 else exit("Cannot use 'put' when stack is empty") 
                else:
                    print(A.pop() if A[-1] not in [True,False] else str(A.pop()).lower()) if len(A) > 0 else exit("Cannot use 'put' when list is empty")

            case 'print':
                if A is None:
                    if len(stack) > 0:
                        if isinstance(stack[-1],str): 
                            print(stack.pop().replace('"', ''))
                        elif isinstance(stack[-1],bool):
                            print(str(stack.pop()).lower())
                        else:
                            print(stack.pop())
                    else:
                        exit("Cannot use 'print' when stack is empty")
                else:
                    if len(A) > 0:
                        if isinstance(A[-1],str): 
                            print(A.pop().replace('"', ''))
                        elif isinstance(A[-1],bool):
                            print(str(A.pop()).lower())
                        else:
                            print(A.pop())
                    else:
                        exit("Cannot use 'print' when list is empty")
                    
            case 'pop':
                if A is None:
                    stack.pop() if len(stack) > 0 else exit("Error: Cannot pop from empty stack")
                else:
                    A.pop() if len(A) > 0 else exit("Error: Cannot pop from empty List")
                
            case 'dup':
                if A is None:
                    stack.append(stack[-1]) if len(stack) > 0 else exit("Error: Cannot duplicate from empty stack")
                else:
                    A.append(A[-1]) if len(A) > 0 else exit("Error: Cannot duplicate from empty list")

            case 'rot':
                if A is None:
                    stack[-1], stack[-2] = stack[-2], stack[-1] if len(stack) >=2 else exit("Error : Not enough elements to rotate in Stack") # Swap top two elements
                else:
                    A[-1], A[-2] = A[-2], A[-1] if len(A) >=2 else exit("Error : Not enough elements to rotate in List") 

            case 'concat':
                if A is None:
                    stack.append(stack.pop(-2) + stack.pop()) if isinstance(stack[-1], str) and isinstance(stack[-2], str) else exit("Error: Cannot concatenate str with incompatible types in Stack")
                else:
                    A.append(A.pop(-2) + A.pop()) if isinstance(A[-1], str) and isinstance(A[-2], str) else exit("Error: Cannot concatenate str with incompatible types in List")

            case 'nth':
                if len(stack) < 2:
                    exit("Error: 'nth' requires a list and an index on the stack")
                index = stack.pop()
                xs = stack.pop()
                if not isinstance(xs, list):
                    exit("Error: 'nth' expects a list as the second-to-top stack item")
                if not isinstance(index, int):
                    exit("Error: 'nth' expects an integer index as the top stack item")
                try:
                    stack.append(xs[index])
                except IndexError:
                    exit(f"Error: Index {index} out of bounds for list of length {len(xs)}")

            case 'spread':
                if isinstance(stack[-1],list):
                    xs = stack.pop()
                    for e in xs:
                        stack.append(e)
                else:
                    exit("There is no list on top of stack")

            case 'stack':
                if A is None:
                    print(stack)
                else:
                    exit("Cannot use 'stack' inside a list")

            case 'true':
                if A is None:
                    stack.append(True)
                else:
                    A.append(True)

            case 'false':
                if A is None:
                    stack.append(False)
                else:
                    A.append(False)

            case '=':
                if A is None:
                    stack.append(stack.pop(-2) == stack.pop()) if is_number(stack[-1]) and is_number(stack[-2]) else exit("Error: Comparison can be only between int/float or same in Stack")
                else:
                    A.append(A.pop(-2) == A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Comparison can be only between int/float or same in List")

            case '<':
                if A is None:
                    stack.append(stack.pop(-2) < stack.pop()) if is_number(stack[-1]) and is_number(stack[-2]) else exit("Error: Comparison can be only between int/float or same in Stack")
                else:
                    A.append(A.pop(-2) < A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Comparison can be only between int/float or same in List")

            case '>':
                if A is None:
                    stack.append(stack.pop(-2) > stack.pop()) if is_number(stack[-1]) and is_number(stack[-2]) else exit("Error: Comparison can be only between int/float or same in Stack")
                else:
                    A.append(A.pop(-2) > A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Comparison can be only between int/float or same in List")

            case '!=':
                if A is None:
                    stack.append(stack.pop(-2) != stack.pop()) if is_number(stack[-1]) and is_number(stack[-2]) else exit("Error: Comparison can be only between int/float or same in Stack")
                else:
                    A.append(A.pop(-2) != A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Comparison can be only between int/float or same in List")

            case '<=':
                if A is None:
                    stack.append(stack.pop(-2) <= stack.pop()) if is_number(stack[-1]) and is_number(stack[-2]) else exit("Error: Comparison can be only between int/float or same in Stack")
                else:
                    A.append(A.pop(-2) <= A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Comparison can be only between int/float or same in List")

            case '>=':
                if A is None:
                    stack.append(stack.pop(-2) >= stack.pop()) if is_number(stack[-1]) and is_number(stack[-2]) else exit("Error: Comparison can be only between int/float or same in Stack")
                else:
                    A.append(A.pop(-2) >= A.pop()) if is_number(A[-1]) and is_number(A[-2]) else exit("Error: Comparison can be only between int/float or same in List")
            
            case 's=':
                if A is None:
                    stack.append(stack.pop(-2) == stack.pop()) if isinstance(stack[-1], str) and isinstance(stack[-2], str) else exit("Error: 's=' expects two strings")      
                else:
                    A.append(A.pop(-2) == A.pop()) if isinstance(A[-1], str) and isinstance(A[-2], str) else exit("Error: 's=' expects two strings in list")

            case 's!=':
                if A is None:
                    stack.append(stack.pop(-2) != stack.pop()) if isinstance(stack[-1], str) and isinstance(stack[-2], str) else exit("Error: 's!=' expects two strings")      
                else:
                    A.append(A.pop(-2) != A.pop()) if isinstance(A[-1], str) and isinstance(A[-2], str) else exit("Error: 's!=' expects two strings in list")

            case 'lex<':
                if A is None:
                    stack.append(stack.pop(-2) < stack.pop()) if isinstance(stack[-1], str) and isinstance(stack[-2], str) else exit("Error: 'lex<' expects two strings")
                else:
                    A.append(A.pop(-2) < A.pop()) if isinstance(A[-1], str) and isinstance(A[-2], str) else exit("Error: 'lex<' expects two strings in list")

            case 'lex>':
                if A is None:
                    stack.append(stack.pop(-2) > stack.pop()) if isinstance(stack[-1], str) and isinstance(stack[-2], str) else exit("Error: 'lex>' expects two strings")
                else:
                    A.append(A.pop(-2) > A.pop()) if isinstance(A[-1], str) and isinstance(A[-2], str) else exit("Error: 'lex>' expects two strings in list")

            case 'lex<=':
                if A is None:
                    stack.append(stack.pop(-2) <= stack.pop()) if isinstance(stack[-1], str) and isinstance(stack[-2], str) else exit("Error: 'lex<=' expects two strings")
                else:
                    A.append(A.pop(-2) <= A.pop()) if isinstance(A[-1], str) and isinstance(A[-2], str) else exit("Error: 'lex<=' expects two strings in list")

            case 'lex>=':
                if A is None:
                    stack.append(stack.pop(-2) >= stack.pop()) if isinstance(stack[-1], str) and isinstance(stack[-2], str) else exit("Error: 'lex>=' expects two strings")
                else:
                    A.append(A.pop(-2) >= A.pop()) if isinstance(A[-1], str) and isinstance(A[-2], str) else exit("Error: 'lex>=' expects two strings in list")

            case 'b=':
                if A is None:
                    stack.append(stack.pop(-2) == stack.pop()) if isinstance(stack[-1], bool) and isinstance(stack[-2], bool) else exit("Error: 'b=' expects two booleans")            
                else:
                    A.append(A.pop(-2) == A.pop()) if isinstance(A[-1], bool) and isinstance(A[-2], bool) else exit("Error: 'b=' expects two booleans in list")
                    

            case 'b!=':
                if A is None:
                    stack.append(stack.pop(-2) != stack.pop()) if isinstance(stack[-1], bool) and isinstance(stack[-2], bool) else exit("Error: 'b=' expects two booleans")            
                else:
                    A.append(A.pop(-2) != A.pop()) if isinstance(A[-1], bool) and isinstance(A[-2], bool) else exit("Error: 'b=' expects two booleans in list")

            case 'dec':
                if A is None:
                    stack.append(stack.pop() - 1) if isinstance(stack[-1], (int,float)) else exit("Cannot decrement non-number values")
                else:
                    A.append(A.pop() -1 ) if isinstance(A[-1],(int,float)) else exit("cannot decrement non-numbers into list")

            case 'inc':
                if A is None:
                    stack.append(stack.pop() + 1) if isinstance(stack[-1], (int,float)) else exit("Cannot decrement non-number values")
                else:
                    A.append(A.pop() + 1 ) if isinstance(A[-1],(int,float)) else exit("cannot decrement non-numbers into list")

            case 'len':
                if A is None:
                    stack.append(len(stack.pop())) if isinstance(stack[-1],list) else exit("Top element of stack is not a list")  
                else:
                    A.append(len(A.pop())) if isinstance(A[-1],list) else exit("Top element of list is not a list")

            case 'listn':
                if A is None:
                    n = stack.pop() if isinstance(stack[-1], int) else exit("listn expects an integer count")
                    if len(stack) < n:
                        exit("Not enough elements on stack for listn")
                    items = [stack.pop() for _ in range(n)][::-1]
                    stack.append(items)
                else:
                    n = A.pop() if isinstance(A[-1], int) else exit("listn expects an integer count")
                    if len(A) < n:
                        exit("Not enough elements in list for listn")
                    items = [A.pop() for _ in range(n)][::-1]
                    A.append(items)

            case "list":
                if A is None:
                    items = stack[:]
                    stack.clear()
                    stack.append(items)
                else:
                    items = A[:]
                    A.clear()
                    A.append(items)

            case 'run':
                if A is None:
                    if isinstance(stack[-1],Program):
                        nucleus(stack.pop().tokens)
                    else:
                        exit("No procedure found! 'run' keyword should be followed by any procedure")
                else:
                    if isinstance(A[-1],Program):
                        nucleus(A.pop().tokens, True)
                    else:
                        exit("No procedure found! 'run' keyword should be followed by any procedure")

            case 'repeat':
                if A is None:
                    if isinstance(stack[-1],Program) and isinstance(stack[-2],int):
                        prg = stack.pop().tokens
                        n = stack.pop()
                        for _ in range(n):
                            nucleus(prg)
                    else:
                        if not isinstance(stack[-1],Program):
                            exit("No procedure found! 'repeat' keyword should be followed by any procedure")
                        else:
                            exit("No count found! 'repeat' keyword should be followed by an positive integer count")
                else:
                    if isinstance(A[-1],Program):
                        nucleus(A.pop().tokens, True)
                    else:
                        exit("No procedure found! 'run' keyword should be followed by any procedure")

            case 'while':
                if A is None:
                    if isinstance(stack[-1],Program) and isinstance(stack[-2],Program):
                        Body = stack.pop().tokens
                        Cond = stack.pop().tokens
                        while True:
                            nucleus(Cond)
                            if stack.pop() == True:
                                nucleus(Body)
                            else:
                                break
                    else:
                        exit("'While' keyword should be followed by a condition and a body")
                        
                else:
                    if isinstance(A[-1],Program) and isinstance(A[-2],Program):
                        Body = A.pop().tokens
                        Cond = A.pop().tokens
                        while nucleus(Cond):
                            nucleus(Body)
                    else:
                        exit("'While' keyword should be followed by a condition and a body")


            case 'if':
                if A is None:
                    if isinstance(stack[-1],Program) and isinstance(stack[-2],Program):
                        Else = stack.pop()
                        Then  = stack.pop()
                        if isinstance(stack[-1],bool):
                            cond = stack.pop()
                            if cond:
                                nucleus(Then.tokens)
                            else:
                                nucleus(Else.tokens)
                        else:
                            exit("if expects a boolean condition")
                    else:
                        exit("if expects a procedure")

                else:
                    if isinstance(A[-1],Program) and isinstance(A[-2],Program):
                        Else = A.pop()
                        Then  = A.pop()
                        if isinstance(A[-1],bool):
                            cond = A.pop()
                            if cond:
                                nucleus(Then.tokens, True)
                            else:
                                nucleus(Else.tokens, True)
                        else:
                            exit("if expects a boolean condition")
                    else:
                        exit("if expects a procedure")





    def nucleus(tokens, flag = False):
        if flag == True:
            A = []
        iter_token = peekable(tokens)
        
        for token in iter_token:
            if token.type == "STRING" and token.value.startswith('"') and token.value.endswith('"'):
                if flag:
                    A.append(token.value) 
                else: 
                    stack.append(token.value) 
                continue

            elif token.type == "NUMBER" and (token.value.lstrip('-').replace('.', '', 1).isdigit()):
                value = float(token.value) if '.' in token.value else int(token.value)
                if flag:
                    A.append(value)
                else:
                    stack.append(value)
                continue

            
            elif token.type == "BRACE" and token.value == '{':
                prg = []
                while iter_token.peek(None) is not None and iter_token.peek().value != '}':
                        prg.append(next(iter_token))
                if iter_token.peek(None) == None:
                    exit("Need curly brace '}' at the end of inner program")
                else:
                    next(iter_token)

                if flag:
                    A.append(Program(tokens = prg))
                else:
                    stack.append(Program(tokens = prg))
                
            elif token.type == "BOOLEAN" and token.value in ("true", "false"):
                if flag:
                    A.append(True if token.value == 'true' else False)  
                else:
                    stack.append(True if token.value == 'true' else False)
                continue

            elif token.type in ("KEYWORD","OPERATOR"):
                if flag:
                    Operation(token.value,A)
                else:
                    Operation(token.value)
                continue
                
            elif token.type == "BRACKET" and token.value == '[':
                L = []
                depth = 1
                while iter_token.peek(None) is not None and depth > 0:
                    next_token = next(iter_token)
                    if next_token.type == "BRACKET":
                        if next_token.value == '[':
                            depth += 1
                        elif next_token.value == ']':
                            depth -= 1
                            if depth == 0:
                                break
                    L.append(next_token)

                if depth != 0:
                    exit("Error : List initialization error. Need matching ']' for '['")

                sublist = nucleus(L, True)
                if flag:
                    A.append(sublist)
                else:
                    stack.append(sublist)
                continue

            else:
                exit(f"Unknown token: {token}")
                return
            
        if flag == True:
            return A
            
    nucleus(tokens)
