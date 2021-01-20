class Solution:
    def singleNumber(self, nums: [int]) -> [int]:
        once = set()
        for n in nums:
            if n not in once:
                once.add(n)
            else:
                once.remove(n)
        return list(once)