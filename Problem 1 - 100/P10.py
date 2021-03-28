class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        recursively match the string 's' with pattern 'p'.
        extract the common factor as first_match
        '''

        if not p:
            return not s

        first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch_improve(self, s: str, p: str) -> bool:
        '''
        improve from the above recursive method,
        instead of using string slicing, use index i, j for 's' and 'p' respectively
        '''

        def sub(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                return sub(i, j+2) or (first_match and sub(i+1, j))
            else:
                return first_match and sub(i+1, j+1)

        return sub(0, 0)

    def isMatch_dp(self, s: str, p: str) -> bool:
        '''
        very naturally from the above method, 
        store result of (i, j) for dynamic programming
        '''

        def sub(i: int, j: int, memo) -> bool:
            if (i, j) not in memo:
                if j == len(p):
                    return i == len(s)

                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                if j+1 < len(p) and p[j+1] == '*':
                    memo[i, j] = sub(i, j+2, memo) or (first_match and sub(i+1, j, memo))
                else:
                    memo[i, j] = first_match and sub(i+1, j+1, memo)
            return memo[i, j]

        return sub(0, 0, {})

s = "aab"
p = "c*a*b"

sol = Solution()
print(sol.isMatch(s, p))
print(sol.isMatch_improve(s, p))
print(sol.isMatch_dp(s, p))