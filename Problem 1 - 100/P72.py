class Solution:
    # naive recursive solution
    def minDistance_naive(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance_naive(word1[1:], word2[1:])
        insert = 1 + self.minDistance_naive(word1, word2[1:])
        delete = 1 + self.minDistance_naive(word1[1:], word2)
        replace = 1 + self.minDistance_naive(word1[1:], word2[1:])
        return min(insert, delete, replace)

    # memoized solution
    # top-down solution
    def minDistance_memo(self, word1: str, word2: str, i: int, j: int, memo: dict) -> int:
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if (i, j) not in memo:
            if word1[i] == word2[j]:
                ans = self.minDistance_memo(word1, word2, i+1, j+1, memo)
            else:
                insert = 1 + self.minDistance_memo(word1, word2, i+1, j, memo)
                delete = 1 + self.minDistance_memo(word1, word2, i, j+1, memo)
                replace = 1 + self.minDistance_memo(word1, word2, i+1, j+1, memo)
                ans = min(insert, delete, replace)
            memo[(i, j)] = ans
        return memo[(i, j)]
        
    # dynamic programming
    # bottom-up solution
    def minDistance_dp(self, word1: str, word2: str):
        m = len(word1) + 1
        n = len(word2) + 1
        table = [[0] * n for _ in range(m)]

        for i in range(m):
            table[i][0] = i
        for j in range(n):
            table[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        return table[-1][-1]

sol = Solution()
# answer = 3
word1 = "pink"
word2 = "sprint"
print(sol.minDistance_naive(word1, word2))
print(sol.minDistance_memo(word1, word2, 0, 0, {}))
print(sol.minDistance_dp(word1, word2))
# answer = 5
word1 = "tompkins"
word2 = "tamping"
print(sol.minDistance_naive(word1, word2))
print(sol.minDistance_memo(word1, word2, 0, 0, {}))   
print(sol.minDistance_dp(word1, word2))