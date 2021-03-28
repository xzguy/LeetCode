class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        checked = dict()
        for i, n in enumerate(nums):
            if target-n in checked:
                return checked[target-n], i
            checked[n] = i
        
num_list = [2, 7, 11, 15, 21, 89]
target = 9
sol = Solution()
print(sol.twoSum(num_list, target))