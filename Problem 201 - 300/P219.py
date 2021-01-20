class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        visited = {}
        for i, n in enumerate(nums):
            if n in visited and i - visited[n] <= k:
                return True
            visited[n] = i
        return False