import collections

class Solution:
    def singleNumber(self, nums: [int]) -> int:
        nums_dict = collections.defaultdict(int)
        for i in nums:
            nums_dict[i] += 1
        for i in nums_dict:
            if nums_dict[i] == 1:
                return i

    def singleNumber_1(self, nums: [int]) -> int:
        ones = twos = 0
        for i in nums:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones
        return ones
       

nums = [0,1,0,1,0,1,99]
sol = Solution()
print(sol.singleNumber(nums))