class Solution:
    # since first and last house can not be robbed at the
    # same time, then divide the problem into two:
    # robbing with first house, robbing with last house
    def rob(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_not_circle(nums[1:]), self.rob_not_circle(nums[:-1]))
        

    def rob_not_circle(self, nums: [int]) -> int:
        first = second = 0
        for n in nums:
            first, second = second, max(second, first + n)
        return second