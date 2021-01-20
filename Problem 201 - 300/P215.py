import heapq

class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        A = [-x for x in nums]
        heapq.heapify(A)
        res = 0
        for _ in range(k):
            res = heapq.heappop(A)
        return -res