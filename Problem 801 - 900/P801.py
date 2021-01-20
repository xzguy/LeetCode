class Solution:
    def minSwap(self, A: [int], B: [int]) -> int:
        # initialize as the first pair, if swap,
        # the number of swaps is 1, otherwise 0
        swap = 1
        not_swap = 0
        for i in range(1, len(A)):
            # in this case, if current pair swap, then
            # the previous pair has to swap
            if A[i] <= B[i-1] or B[i] <= A[i-1]:
                new_swap = swap + 1
                new_not_swap = not_swap
            # in this case, either the current or the previous
            # pair should swap
            elif A[i] <= A[i-1] or B[i] <= B[i-1]:
                new_swap = not_swap + 1
                new_not_swap = swap
            # in this case, either swap or not is ok
            else:
                new_not_swap = min(swap, not_swap)
                new_swap = new_not_swap + 1
            swap = new_swap
            not_swap = new_not_swap
        return min(swap, not_swap)

A = [1,3,5,4]
B = [1,2,3,7]
sol = Solution()
print(sol.minSwap(A, B))