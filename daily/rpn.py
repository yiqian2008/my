import sys

def rpn(tokens):
    stack = []
    operations = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operations:
            if len(stack) < 2:
                raise RuntimeError(f": Not enough arguments for {token} operator.")   
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            stack.append(result)
        else:
            try:
                num = float(token)
            except ValueError:
                raise ValueError(f"could not convert string to float: '{token}'")
            stack.append(num)
    if len(stack) != 1:
        raise RuntimeError("Not enough operators; too many elements on remained on stack.")
    return stack[0]

if __name__ == "__main__":                  # a suggested way to define the main part of a script
    print (rpn( sys.argv[1:] ))