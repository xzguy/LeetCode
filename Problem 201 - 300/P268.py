class Solution:
    # summation from 0 to n is n*(n+1)/2
    def missingNumber(self, nums: [int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)