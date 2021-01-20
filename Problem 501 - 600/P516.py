class Solution:
    # recursive
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def sub(l: int, r: int) -> int:
            if l == r:
                return 1
            if l > r:
                return 0
            if s[i] == s[r]:
                return 2 + sub(l+1, r-1)
            else:
                return max(sub(l+1, r), sub(l, r-1))
        
        return sub(0, len(s)-1)

    # dp with memo
    def longestPalindromeSubseq_1(self, s: str) -> int:
        
        def sub(l: int, r: int, memo: dict) -> int:
            if l == r:
                return 1
            if l > r:
                return 0
            if (l, r) not in memo:
                if s[l] == s[r]:
                    res = 2 + sub(l+1, r-1, memo)
                else:
                    res = max(sub(l+1, r, memo), sub(l, r-1, memo))
                memo[l, r] = res
            return memo[l, r]

        return sub(0, len(s)-1, {})

    # dp bottom up
    def longestPalindromeSubseq_2(self, s: str) -> int:
        N = len(s)
        dp = [[0] * N for _ in range(N+1)]
        # length of 1 is palindrome
        for i in range(N):
            dp[1][i] = 1
        # length
        for l in range(2, N+1):
            for i in range(N-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[l][i] = 2 + dp[l-2][i+1]
                else:
                    dp[l][i] = max(dp[l-1][i], dp[l-1][i+1])
        return dp[N][0]