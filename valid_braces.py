def valid_braces(string):
    pairs = { ')': '(',
        ']': '[',
        '}': '{' }

    stack = []

    for brace in string:
        if brace in "([{":
            stack.append(brace)
        else:
            if not stack:
                return False

            last_open = stack.pop()

            if last_open != pairs[brace]:
                return False

    return len(stack) == 0
