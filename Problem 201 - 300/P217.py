class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)
        return False