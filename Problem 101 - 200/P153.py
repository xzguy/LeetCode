class Solution:
    '''
    The problem assumes there can be 0 or 1 rotation!
    '''
    def findMin(self, nums: [int]) -> int:
        # if there is no rotation
        if nums[-1] >= nums[0]:
            return nums[0]
        # since there is a rotation, maximum appear ahead of minimum
        max_idx = 0
        min_idx = len(nums)-1
        while max_idx+1 < min_idx:
            mid = (max_idx + min_idx) // 2
            if nums[max_idx] < nums[mid]:
                max_idx = mid
            else:
                min_idx = mid
        return nums[min_idx]

sol = Solution()
input = [4,5,6,7,0,1,2]
input = [1,2]
print(sol.findMin(input))