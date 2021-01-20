class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

sol = Solution()
nums = [1,2,3,4,5,6,7]
k = 3
print(sol.rotate(nums, k))