class Solution:
    def canThreePartsEqualSum(self, A: [int]) -> bool:
        summation = sum(A)
        if summation % 3 > 0:
            return False
        sum_single = summation // 3
        partitions = 0
        for a in A:
            if sum_single - a == 0:
                sum_single = summation // 3
                partitions += 1
            else:
                sum_single -= a
        # if the summation is zero, partitions could be more than 3
        return partitions >= 3