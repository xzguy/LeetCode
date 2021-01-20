class Solution:
    def search(self, nums: [int], target: int) -> bool:
        if not nums:
            return False
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return True
            if nums[m] == nums[l] and nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False

nums = [1,3,1,1]
target = 3
sol = Solution()
print(sol.search(nums, target))