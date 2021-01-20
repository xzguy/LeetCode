import collections

class Solution:
    # brute force, not efficient
    def subarraysWithKDistinct(self, A: [int], K: int) -> int:
        N = len(A)
        res = 0
        for i in range(N):
            for j in range(i+1, N+1):
                if len(set(A[i:j])) == K:
                    res += 1
        return res

    # sliding window, maintain the counter of the current window
    def subarraysWithKDistinct_1(self, A: [int], K: int) -> int:
        N = len(A)
        res = 0
        window = collections.defaultdict(int)
        num_unique = 0
        # window's left and right pointers are inclusive
        l = r = 0
        while r < N:

            while r < N and num_unique <= K:
                window[A[r]] += 1
                if window[A[r]] == 1:
                    num_unique += 1
                r += 1
                if num_unique == K:
                    res += 1
                    if r == N or window[A[r]] == 0:
                        break

            while l < r and num_unique == K:
                if window[A[l]] == 1:
                    num_unique -= 1
                window[A[l]] -= 1
                if num_unique == K:
                    res += 1
                l += 1
        
        return res

A = [1,2,1,2,3]
K = 2
sol = Solution()
print(sol.subarraysWithKDistinct_1(A, K))