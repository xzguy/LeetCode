class Solution:
    # from right to left, or 
    # least significant digit to most significant digit
    def titleToNumber(self, s: str) -> int:
        exp = 1
        res = 0
        for i in range(len(s)-1, -1, -1):
            res += (ord(s[i]) - ord('A') + 1) * exp
            exp *= 26
        return res

    # this is the reverse of the above method
    def titleToNumber_1(self, s: str) -> int:
        res = 0
        for c in s:
            res = res * 26 + ord(c) - ord('A') + 1
        return res

sol = Solution()

input = "ZY"
input = "AB"
print(sol.titleToNumber_1(input))