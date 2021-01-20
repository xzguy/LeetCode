class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        if len(nums) < 2:
            return 0

        N = len(nums)
        # most left index of unsorted number
        left = N-1
        # most right index of unsorted number
        right = 0
        stack = []
        for i in range(N):
            while stack and nums[i] < nums[stack[-1]]:
                idx = stack.pop()
                left = min(left, idx)
            stack.append(i)
        stack = []
        for i in range(N-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                right = max(right, idx)
            stack.append(i)
        if left < right:
            return right - left + 1
        return 0