class Solution:
    def longestOnes(self, A: [int], K: int) -> int:
        if not A:
            return 0
        left, right = 0, 0
        max_con_ones = 0
        cur_zero = 0
        while right < len(A):
            if A[right] == 0:
                if cur_zero < K:
                    cur_zero += 1
                else:
                    cur_con_ones = right-left
                    max_con_ones = max(max_con_ones, cur_con_ones)
                    while A[left] != 0:
                        left += 1
                    left += 1
            right += 1
        cur_con_ones = right-left
        max_con_ones = max(max_con_ones, cur_con_ones)
        return max_con_ones

    def longestOnes_1(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return len(A) - i

sol = Solution()
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(sol.longestOnes_1(A, K))