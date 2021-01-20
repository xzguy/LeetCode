class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        while n not in num_set:
            num_set.add(n)
            n = self.sum_square_digits(n)
            if n == 1:
                return True
        return False

    def sum_square_digits(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n%10)**2
            n //= 10
        return res

sol = Solution()
print(sol.isHappy(37))