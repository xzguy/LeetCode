import math

class Solution:
    def soupServings(self, N: int) -> float:
        if N > 4800:
            return 1

        def sub(a: int, b: int, memo: dict) -> int:
            if (a, b) not in memo:
                if a <= 0 and b <= 0:
                    # half of the probability that A and B finish together
                    return 0.5
                if a <= 0:
                    return 1
                if b <= 0:
                    return 0
                memo[a,b] = 0.25 * (sub(a-4, b, memo) + sub(a-3, b-1, memo) + sub(a-2, b-2, memo) + sub(a-1, b-3, memo))
            return memo[a,b]

        N = math.ceil(N / 25)
        return sub(N, N, {})