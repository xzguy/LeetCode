class Solution:
    def findPeakElement(self, nums: [int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l + r) // 2
            # if there is an increase after mid,
            # then there must be peak after mid
            if nums[mid] < nums[mid+1]:
                l = mid+1
            # if there is a decrease after mid,
            # then there must be a peak before mid
            else:
                r = mid
        return l

nums = [1,2,1,3,5,6,4]
sol = Solution()
print(sol.findPeakElement(nums))