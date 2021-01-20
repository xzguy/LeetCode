class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        if not nums:
            return []

        start = 0
        res = []
        while start < len(nums):
            end = start+1
            while end < len(nums) and nums[end] == nums[end-1]+1:
                end += 1
            if start == end-1:
                res.append(str(nums[start]))
            else:
                res.append(str(nums[start]) + "->" + str(nums[end-1]))
            start = end
        return res