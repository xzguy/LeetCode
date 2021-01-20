class Solution:
    # only a pair of factor 2 and 5 can contribute
    # to trailing zeros. In factorial, 2 is much
    # more than 5. So we only need to consider 5.
    def trailingZeroes(self, n: int) -> int:
        res = 0
        factor_5 = 5
        while factor_5 <= n:
            res += n // factor_5
            factor_5 *= 5
        return res

sol = Solution()
print(sol.trailingZeroes(30))