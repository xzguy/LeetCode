class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        stack = []
        begin_primitive = False
        for s in S:
            if s == "(":
                if begin_primitive:
                    stack.append(s)
                    res += s
                if not stack:
                    begin_primitive = True
            else:
                if not stack:
                    begin_primitive = False
                else:
                    res += ")"
                    stack.pop()
        return res