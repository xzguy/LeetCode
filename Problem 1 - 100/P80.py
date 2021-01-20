class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) < 2:
            return nums
        last_1, last_2 = nums[1], nums[0]
        i = 2
        while i <len(nums):
            if nums[i] == last_1 and nums[i] == last_2:
                nums.remove(last_1)
            else:
                last_2 = last_1
                last_1 = nums[i]
                i += 1
        return len(nums)
            
nums = [0,0,1,1,1,1,2,3,3]
sol = Solution()
print(sol.removeDuplicates(nums))