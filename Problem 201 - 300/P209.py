class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        l, r = 0, 0
        min_len = float('inf')
        while r < len(nums):
            if sum(nums[l:r+1]) < s:
                r += 1
            else:
                min_len = min(min_len, r-l+1)
                l += 1
        if min_len > len(nums):
            return 0
        return min_len

    # remove the sum() of subarray in the above method
    def minSubArrayLen_1(self, s: int, nums: [int]) -> int:
        l = 0
        min_len = float('inf')
        win_sum = 0
        for i in range(len(nums)):
            win_sum += nums[i]
            while win_sum >= s:
                min_len = min(min_len, i+1-l)
                win_sum -= nums[l]
                l += 1
        if min_len > len(nums):
            return 0
        return min_len