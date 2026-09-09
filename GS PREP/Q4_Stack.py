def parenthesis(s):
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i in bracket_map:

            if len(stack) != 0:
                top = stack.pop()
            else:
                return False
            if bracket_map[i] != top:
                return False
        else:
            stack.append(i)
    return len(stack) == 0