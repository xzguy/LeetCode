class Solution:
    def numMovesStonesII(self, stones: [int]) -> [int]:
        A = sorted(stones)
        i = 0
        n = len(A)
        # upper bound for low (inclusive)
        low = len(A)-1
        for j in range(n):
            while A[j] - A[i] >= n:
                i += 1
            # corner case
            if j - i + 1 == n-1 and A[j] - A[i] + 1 == n-1:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        high = max(A[-1] - A[1] - n + 2, A[-2] - A[0] - n + 2)
        return [low, high]