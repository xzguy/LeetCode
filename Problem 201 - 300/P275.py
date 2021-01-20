class Solution:
    def hIndex(self, citations: [int]) -> int:
        N = len(citations)
        i = N-1
        while i >= 0:
            if citations[i] >= N - i:
                i -= 1
            else:
                break
        return N-1-i

    # binary search
    def hIndex_1(self, citations: [int]) -> int:
        N = len(citations)
        l = 0
        r = N
        while l < r:
            mid = (l + r) // 2
            if citations[mid] >= N - mid:
                r = mid
            else:
                l = mid + 1
        return N - r