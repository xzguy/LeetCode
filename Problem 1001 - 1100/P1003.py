class Solution:
    # recursive
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        for i in range(len(s)-2):
            if s[i:i+3] == "abc":
                new_str = s[:i] + s[i+3:]
                return self.isValid(new_str)
        return False

    # iterative with stack
    def isValid_1(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == 'c':
                if len(stack) < 2:
                    return False
                if stack.pop() != 'b':
                    return False
                if stack.pop() != 'a':
                    return False
            else:
                stack.append(s[i])
        return not stack


sol = Solution()
s = "abcabcababcc"
s = "cababc"
s = "abccba"
s = "aabcbc"
print(sol.isValid_1(s))