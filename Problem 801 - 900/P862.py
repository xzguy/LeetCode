import collections

class Solution:
    # K >= 1, len(A) >= 1
    # brute force
    def shortestSubarray(self, A: [int], K: int) -> int:
        # get the cumulative array, append 0 at the front
        for i in range(1, len(A)):
            A[i] += A[i-1]
        A = [0] + A

        # initialize an impossible value
        shortest_sub = len(A)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[j]-A[i] >= K:
                    shortest_sub = min(shortest_sub, j-i)
                    break
        if shortest_sub == len(A):
            return -1
        return shortest_sub

    # monotonic queue with sliding window
    def shortestSubarray_1(self, A: [int], K: int) -> int:
        # get the cumulative array, append 0 at the front
        for i in range(1, len(A)):
            A[i] += A[i-1]
        A = [0] + A

        # initialize an impossible value
        shortest_sub = len(A)
        monoq = collections.deque()
        for i in range(len(A)):
            while monoq and A[i] <= A[monoq[-1]]:
                monoq.pop()
            
            while monoq and A[i] - A[monoq[0]] >= K:
                idx = monoq.popleft()
                shortest_sub = min(shortest_sub, i - idx)

            monoq.append(i)
        return shortest_sub if shortest_sub != len(A) else -1