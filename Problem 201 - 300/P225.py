class Solution:
    '''
    scan the string, if "+" and "-", put it into a stack
    if "*" and "/", pop a number from stack, finish calculation, then push
    result into the stack.
    At last, pop the stack one by one and finish all "+" and "-" calculation.
    '''
    def calculate(self, s: str) -> int:
        stack = []
        num, idx = self.get_next_number(s, 0)
        stack.append(num)
        if idx == len(s):
            return num
        while idx < len(s):
            operator, idx = self.get_next_operator(s, idx)
            num, idx = self.get_next_number(s, idx)
            if operator in "*/":
                num_1 = stack.pop()
                if operator == "*":
                    num = num * num_1
                else:
                    num = int(num_1 / num)
                stack.append(num)
            elif operator in "+-":
                stack.append(operator)
                stack.append(num)
            else:
                # reach the end of string, the operator is '@'
                pass

        # empty the stack
        res = 0
        while len(stack) > 1:
            num = stack.pop()
            operator = stack.pop()
            if operator == "+":
                res += num
            else:
                res -= num
        return res + stack.pop()

    def get_next_number(self, s: str, start_idx: int) -> [int]:
        start_number = False
        i = start_idx
        while i < len(s):
            if not start_number and s[i] in "0123456789":
                start_number = True
                start_idx = i
            if start_number and s[i] not in "0123456789":
                break
            i += 1
        if start_idx == i:
            return [None, i]
        return [int(s[start_idx:i]), i]
    
    def get_next_operator(self, s: str, start_idx: int) -> [int]:
        while start_idx < len(s):
            if s[start_idx] in "+-*/":
                return [s[start_idx], start_idx+1]
            start_idx += 1
        return ["@", start_idx]

s = " 3/2 "
sol = Solution()
print(sol.calculate(s))