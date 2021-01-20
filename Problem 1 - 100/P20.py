def isValid(s: str) -> bool:
    parentheses_dict = {'(': ')', '[': ']', '{': '}'}
    input = list(s)
    
    stack = []

    for p in input:
        if p in parentheses_dict:
            stack.append(p)
        else:
            if not stack or p != parentheses_dict[stack[-1]]:
                return False
            else:
                stack.pop()
    return len(stack) == 0

input = "]"

print(isValid(input))