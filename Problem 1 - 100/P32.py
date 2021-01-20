'''
Analysis:
    count open and closing parentheses from both direction
'''
def longestValidParentheses_two_tranverse(s: str) -> int:
    max_len = 0
    # tranverse from left to right
    op = cp = 0
    for c in s:
        if c == '(': op += 1
        elif c == ')': cp += 1
        else: raise ValueError

        if op == cp: max_len = max(op+cp, max_len)
        if op < cp: op = cp = 0
    # tranverse from right to left
    op = cp = 0
    for c in reversed(list(s)):
        if c == '(': op += 1
        elif c == ')': cp += 1
        else: raise ValueError

        if op == cp: max_len = max(op+cp, max_len)
        if op > cp: op = cp = 0
    return max_len
        
'''
Analysis:
    maintain an integer array with same length of input string
the number at index i, should be the maximum length of well
formatted substring ending with character at index i in input
string.
'''
def longestValidParentheses_dp(s: str) -> int:
    max_len = 0
    dp_array = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i-1] == '(':
                dp_array[i] = dp_array[i-2] + 2 if i>=2 else 2
            elif s[i-1] == ')':
                if i - dp_array[i-1] > 0 and s[i - dp_array[i-1] - 1] == '(':
                    if i - dp_array[i-1] - 2 >= 0:
                        dp_array[i] = dp_array[i-1] + dp_array[i-dp_array[i-1]-2] + 2
                    else:
                        dp_array[i] = dp_array[i-1] + 2
            else:
                raise ValueError
            max_len = max(dp_array[i], max_len)
    return max_len

'''
Analysis:
    use stack to store character's index!!
'''
def longestValidParentheses_stack(s: str) -> int:
    stack = [-1]
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            stack.pop()
            if len(stack) > 0:
                max_len = max(i-stack[-1], max_len)
            else:
                stack.append(i)
    return max_len

s1 = "()(())"
s2 = "()(()"
s3 = ")()())"
s4 = ")()(((())))("
s5 = "(()(((()"
print(longestValidParentheses_stack(s5))