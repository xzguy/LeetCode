class Solution:
    def findMin(self, nums: [int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[lo]:
                hi = mid
                lo += 1
            else:
                # nums[lo] <= nums[mid] <= nums[hi]
                hi -= 1
        return nums[lo]

sol = Solution()
input = [4,5,6,7,0,1,2]
input = [1,2]
input = [2,2,2,0,0,0,0,1,1,1,1]
input = [3,1,3,3,3,3]
print(sol.findMin(input))
        