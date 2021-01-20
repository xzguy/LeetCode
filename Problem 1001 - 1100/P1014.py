class Solution:
    def maxScoreSightseeingPair_1(self, A: [int]) -> int:
        max_score = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                max_score = max(max_score, A[i]+A[j]+i-j)
        return max_score

    def maxScoreSightseeingPair(self, A: [int]) -> int:
        pre_max = float('-inf')
        max_score = 0
        for i in range(len(A)-1):
            if A[i]+i > pre_max:
                pre_max = A[i]+i
            max_score = max(max_score, pre_max + A[i+1]-(i+1))
        return max_score