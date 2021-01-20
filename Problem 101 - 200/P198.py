class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        # initialize second item
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            if nums[i-2] + nums[i] > nums[i-1]:
                nums[i] = nums[i-2] + nums[i]
            else:
                nums[i] = nums[i-1]
        return max(nums[-1], nums[-2])

    '''
    This is the same as the above solution,
    but use two extra variables to avoid edge case
    for the first two items in the array
    '''
    def rob_1(self, nums: [int]) -> int:
        first = second = 0
        for n in nums:
            first, second = second, max(second, first + n)
        return second

    def rob_2(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


sol = Solution()
nums = [1,2,3,1]
print(sol.rob_1(nums))