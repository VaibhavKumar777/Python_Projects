def is_paired(input_string):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in input_string:
        if char in "({[":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0
