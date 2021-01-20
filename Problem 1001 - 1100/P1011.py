import math

class Solution:
    def shipWithinDays(self, weights: [int], D: int) -> int:
        capacity = max(weights)
        capacity = max(capacity, math.ceil(sum(weights)/D))
        while not self.isValid(weights, D, capacity):
            capacity += 1
        return capacity

    def isValid(self, weights: [int], D: int, capacity: int) -> bool:
        w_idx = 0
        for _ in range(D):
            total = 0
            while w_idx < len(weights) and total + weights[w_idx] <= capacity:
                total += weights[w_idx]
                w_idx += 1
        if w_idx == len(weights):
            return True
        else:
            return False

    # binary search
    def shipWithinDays_1(self, weights, D):
        low = max(weights)
        low = max(low, math.ceil(sum(weights)/D))
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            need = 1
            cur = 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                low = mid + 1
            else: 
                high = mid
        return low