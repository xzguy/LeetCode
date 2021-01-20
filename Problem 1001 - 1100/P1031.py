class Solution:
    def maxSumTwoNoOverlap(self, A: [int], L: int, M: int) -> int:
        cur = sum(A[:L])
        res = cur + self.maxSumSubarray(A[L:], M)
        for i in range(1, len(A)-L+1):
            cur -= A[i-1]
            cur += A[i+L-1]
            subarray_M = max(self.maxSumSubarray(A[:i], M), self.maxSumSubarray(A[i+L:], M))
            res = max(res, cur+subarray_M)
        return res

    def maxSumSubarray(self, A: [int], M: int) -> int:
        if len(A) < M:
            return float('-inf')
        cur = sum(A[:M])
        res = cur
        for i in range(1, len(A)-M+1):
            cur -= A[i-1]
            cur += A[i+M-1]
            res = max(res, cur)
        return res

    # when calculate the sum of subarray, it is better
    # to convert the array into accumulated one first.
    def maxSumTwoNoOverlap_1(self, A: [int], L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[i-1]
        res = A[L + M -1]
        L_max = A[L-1]
        M_max = A[M-1]
        for i in range(L+M, len(A)):
            # if L is before M, update L subarray maximum
            cur_L_max = A[i-M] - A[i-M-L]
            L_max = max(L_max, cur_L_max)
            # if M is before L, update M subarray maximum
            cur_M_max = A[i-L] - A[i-L-M]
            M_max = max(M_max, cur_M_max)
            # if L is before M
            L_M = L_max + A[i] - A[i-M]
            # if M is before L
            M_L = M_max + A[i] - A[i-L]
            res = max(res, L_M, M_L)
        return res