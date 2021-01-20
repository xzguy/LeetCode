class Solution:
    # naive recursive
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        if text1[0] == text2[0]:
            return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        else:
            return max(self.longestCommonSubsequence(text1[1:], text2), self.longestCommonSubsequence(text1, text2[1:]))

    # dp memo
    def longestCommonSubsequence_1(self, text1: str, text2: str) -> int:

        def sub(t1_idx: int, t2_idx: int, memo: dict) -> int:
            if t1_idx == len(text1) or t2_idx == len(text2):
                return 0
            
            if (t1_idx, t2_idx) not in memo:
                if text1[t1_idx] == text2[t2_idx]:
                    res = 1 + sub(t1_idx+1, t2_idx+1, memo)
                else:
                    res = max(sub(t1_idx+1, t2_idx, memo), sub(t1_idx, t2_idx+1, memo))
                memo[t1_idx, t2_idx] = res
            return memo[t1_idx, t2_idx]
        
        return sub(0, 0, {})

    # dp bottom up
    # dp[i][j] is the longest common subsequence between text1[:i+1] and text2[:j+1]
    def longestCommonSubsequence_2(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        M = len(text1)
        N = len(text2)
        dp = [[0] * (N+1) for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

