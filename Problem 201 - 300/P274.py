import heapq

class Solution:
    def hIndex(self, citations: [int]) -> int:
        citations.sort()
        N = len(citations)
        i = N-1
        while i >= 0:
            if citations[i] >= N-i:
                i -= 1
            else:
                break
        return N-1-i

    # binary search
    def hIndex_1(self, citations: [int]) -> int:
        citations.sort()
        N = len(citations)
        l = 0
        r = N
        while l < r:
            mid = (l+r)//2
            if citations[mid] >= N-mid:
                r = mid
            else:
                l = mid + 1
        # finally l == r, and citations[r] is the minimum citations included
        return N-r

    # heap, not sort
    def hIndex_2(self, citations: [int]) -> int:
        # since python heapq is min-heap, convert it to negative
        A = [-x for x in citations]
        heapq.heapify(A)
        i = 1
        while A and -heapq.heappop(A) >= i:
            i += 1
        return i-1

citations = [1]
citations = [3,0,6,1,5]
sol = Solution()
print(sol.hIndex_2(citations))