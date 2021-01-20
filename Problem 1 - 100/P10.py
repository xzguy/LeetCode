class Solution:
    def isMatch_rec(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch_rec(s, p[2:]) or (first_match and self.isMatch_rec(s[1:], p))
        else:
            return first_match and self.isMatch_rec(s[1:], p[1:])

    def isMatch_dp(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i: int, j: int) -> bool:
            if (i, j) not in memo:
                if j == len(p):
                    ans = (i == len(s))
                else:
                    first_match = (i < len(s)) and p[j] in {s[i], '.'}

                    if j+1 < len(p) and p[j+1] == '*':
                        return dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        return first_match and dp(i+1, j+1)
                memo[(i, j)] = ans
            return memo[(i, j)]
        return dp(0, 0)

s = "aab"
p = "c*a*b"

sol = Solution()
print(sol.isMatch_rec(s, p))