class Solution:
    def majorityElement(self, nums: [int]) -> int:
        maj = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cnt == 0:
                maj = nums[i]
            if nums[i] != maj:
                cnt -= 1
            else:
                cnt += 1
        return maj

sol = Solution()
input = [2,2,1,1,1,2,2]
input = [3,2,3]
print(sol.majorityElement(input))
        