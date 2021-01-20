class Solution:
    # recursive method wtih greedy
    def maxUncrossedLines(self, A: [int], B: [int]) -> int:
        if not A or not B:
            return 0
        connect = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    connect = max(connect, 1 + self.maxUncrossedLines(A[i+1:], B[j+1:]))
                    break
        return connect
    
    # dynamic programming, for 0 <= a < len(A), 0 <= b < len(B),
    # dp[a][b] means the number of connections between A[:a+1] and B[:b+1]
    # for dp[a][b], if A[a] == B[b]: dp[a][b] = 1 + dp[a-1][b-1]
    # else: dp[a][b] = max(dp[a-1][b], dp[a][b-1])
    def maxUncrossedLines_1(self, A: [int], B: [int]) -> int:
        if not A or not B:
            return 0
        dp = [[0 for _ in range(len(A))] for _ in range(len(B))]
        # initialize first row and first column
        for i in range(len(A)):
            if B[0] == A[i]:
                dp[0][i] = 1
                for k in range(i+1, len(A)):
                    dp[0][k] = 1
                break
        for j in range(len(B)):
            if A[0] == B[j]:
                dp[j][0] = 1
                for k in range(j+1, len(B)):
                    dp[k][0] = 1
                break

        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        return dp[-1][-1]


A = [2,5,1,2,5]
B = [10,5,2,1,5,2]
sol = Solution()
print(sol.maxUncrossedLines_1(A, B))