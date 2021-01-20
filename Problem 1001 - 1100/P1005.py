class Solution:
    def largestSumAfterKNegations(self, A: [int], K: int) -> int:
        if not A:
            return 0
        positive_zero_part = [x for x in A if x >= 0]
        negative_part = [x for x in A if x < 0]
        positive_zero_part.sort()
        negative_part.sort()
        if K <= len(negative_part):
            for i in range(K):
                negative_part[i] = -negative_part[i]
            return sum(positive_zero_part) + sum(negative_part)
        else:
            all_pos_sum = sum(positive_zero_part) - sum(negative_part)
            if 0 not in positive_zero_part and \
                (K - len(negative_part)) % 2 == 1:
                if len(negative_part) == 0:
                    return all_pos_sum - 2*positive_zero_part[0]
                if len(positive_zero_part) == 0:
                    return all_pos_sum + 2*negative_part[-1]
                return all_pos_sum - 2*min(positive_zero_part[0], -negative_part[-1])
        return all_pos_sum

    def largestSumAfterKNegations_1(self, A, K):
        A.sort()
        i = 0
        # from smallest negative number, 
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2

A = [4,2,3]
K = 1
A = [3,-1,0,2]
K = 3
A = [2,-3,-1,5,-4]
K = 2
sol = Solution()
print(sol.largestSumAfterKNegations(A, K))