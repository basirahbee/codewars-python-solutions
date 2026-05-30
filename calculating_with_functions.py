def calculate(left, op):
    operator, right = op

    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        return left // right

def zero(op=None):
    return 0 if op is None else calculate(0, op)

def one(op=None):
    return 1 if op is None else calculate(1, op)

def two(op=None):
    return 2 if op is None else calculate(2, op)

def three(op=None):
    return 3 if op is None else calculate(3, op)

def four(op=None):
    return 4 if op is None else calculate(4, op)

def five(op=None):
    return 5 if op is None else calculate(5, op)

def six(op=None):
    return 6 if op is None else calculate(6, op)

def seven(op=None):
    return 7 if op is None else calculate(7, op)

def eight(op=None):
    return 8 if op is None else calculate(8, op)

def nine(op=None):
    return 9 if op is None else calculate(9, op)

def plus(num):
    return ("+", num)

def minus(num):
    return ("-", num)

def times(num):
    return ("*", num)

def divided_by(num):
    return ("/", num)
