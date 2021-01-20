'''
has a list with same length of the input,
initialize it with all ones.
if number is greater than the pivot one, increment its length by one
'''

class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        N = len(nums)

        longest_seq_len = [1] * N
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[j] > nums[i] and longest_seq_len[j] < longest_seq_len[i]+1:
                    longest_seq_len[j] = longest_seq_len[i]+1
        return max(longest_seq_len)

    # binary search
    def lengthOfLIS_1(self, nums: [int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j)//2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(size, i+1)
        return size