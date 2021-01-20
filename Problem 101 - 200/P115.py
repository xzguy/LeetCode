class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        res = 0
        for i in range(len(s) - len(t) + 1):
            if s[i] == t[0]:
                res += self.numDistinct(s[i+1:], t[1:])
        return res

    # instead of generate new sub-string, use index
    def numDistinct_1(self, s: str, t: str) -> int:

        def sub(s_start: int, t_start: int) -> int:
            if t_start == len(t):
                return 1
            res = 0
            for i in range(s_start, len(s)):
                if s[i] == t[t_start]:
                    res += sub(i+1, t_start+1)
            return res

        return sub(0, 0)
        
    # use memo to store the intermediate result
    def numDistinct_2(self, s: str, t: str) -> int:

        def sub(s_start: int, t_start: int, memo) -> int:
            if (s_start, t_start) not in memo:
                if t_start == len(t):
                    return 1
                res = 0
                for i in range(s_start, len(s)):
                    if s[i] == t[t_start]:
                        res += sub(i+1, t_start+1, memo)
                memo[(s_start, t_start)] = res
            return memo[(s_start, t_start)]
            
        return sub(0, 0, {})
    
    # dynamic programming/bottom up solution
    def numDistinct_3(self, s: str, t: str) -> int:
        mat = [[0 for _ in range(len(s))] for _ in range(len(t))]
        # initialize first row
        for col in range(len(s)-len(t)+1):
            if t[0] == s[col]:
                mat[0][col] = 1
        # finish the table
        for row in range(1, len(t)):
            for col in range(row, len(s)-len(t)+row+1):
                if t[row] == s[col]:
                    mat[row][col] = sum(mat[row-1][:col])
        return sum(mat[-1])

sol = Solution()
S = "rabbbit"
T = "rabbit"

S = "babgbag"
T = "bag"
print(sol.numDistinct_3(S, T))