class Solution:
    # brute force solution
    def longestArithSeqLength(self, A: [int]) -> int:
        if len(A) < 3:
            return len(A)
        longest_arithmetic = 2
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                diff = A[j] - A[i]
                num = 2
                for k in range(j+1, len(A)):
                    if A[k] == A[i] + num*diff:
                        num += 1
                if num > longest_arithmetic:
                    longest_arithmetic = num
        return longest_arithmetic

    # dynamic programming
    # dp[index][diff] equals to the length of arithmetic sequence
    # at index with difference diff.
    def longestArithSeqLength_1(self, A: [int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dp[j, A[j]-A[i]] = dp.get((i, A[j]-A[i]), 1) + 1
        return max(dp.values())

sol = Solution()
nums = [3,6,9,12]
print(sol.longestArithSeqLength_1(nums))