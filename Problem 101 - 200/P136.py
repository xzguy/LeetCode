class Solution:
    def singleNumber(self, nums: [int]) -> int:
        num_set = set()
        for i in nums:
            if i not in num_set:
                num_set.add(i)
            else:
                num_set.remove(i)
        return num_set.pop()

    def singleNumber_1(self, nums: [int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

nums = [4,1,2,1,2]
sol = Solution()
print(sol.singleNumber_1(nums))
        