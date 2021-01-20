import math

class Solution:
    # recursive, from right to left
    def evalRPN(self, tokens: [str]) -> int:
        if tokens[-1] not in ["+", "-", "*", "/"]:
            return int(tokens[-1])
        operator = tokens[-1]
        num_cnt = 0
        j = len(tokens)-1
        while num_cnt != 1:
            if tokens[j-1] in ["+", "-", "*", "/"]:
                num_cnt -= 1
            else:
                num_cnt += 1
            j -= 1
        if operator == "+":
            return self.evalRPN(tokens[:j]) + self.evalRPN(tokens[j:len(tokens)-1])
        if operator == "-":
            return self.evalRPN(tokens[:j]) - self.evalRPN(tokens[j:len(tokens)-1])
        if operator == "*":
            return self.evalRPN(tokens[:j]) * self.evalRPN(tokens[j:len(tokens)-1])
        if operator == "/":
            res = self.evalRPN(tokens[:j]) / self.evalRPN(tokens[j:len(tokens)-1])
            if res >= 0:   
                return math.floor(res)
            else:
                return math.ceil(res)
        
    # using stack, from left to right parse
    def evalRPN_1(self, tokens: [str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if t == "+":
                    stack.append(operand_1 + operand_2)
                if t == "-":
                    stack.append(operand_1 - operand_2)
                if t == "*":
                    stack.append(operand_1 * operand_2)
                if t == "/":
                    stack.append(int(operand_1 / operand_2))
            else:
                stack.append(int(t))
        return stack.pop()

sol = Solution()
input = ["2", "1", "+", "3", "*"]
input = ["4", "13", "5", "/", "+"]
input = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(sol.evalRPN_1(input))
print(2/4)
print(2//4)
print(math.floor(2/4))
print(int(2/4))
# math.floor() is same as "//"
# int() is rounding to zero for both positive and negative,
# otherwise, for positive, int() is math.floor(); for negative int() is math.ceil()
print(-2/4)
print(-2//4)
print(math.floor(-2/4))
print(int(-2/4))