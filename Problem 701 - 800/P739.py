class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        nums = T
        if not nums:
            return []
        warmer = [0] * len(nums)
        stack = [0]
        for i in range(1, len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                warmer[idx] = i - idx
            stack.append(i)
        return warmer