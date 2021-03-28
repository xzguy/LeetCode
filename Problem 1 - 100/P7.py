class Solution:
    '''
    The key point in this problem is to avoid overflow.
    '''
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        max_int_digit = MAX_INT % 10
        min_int_digit = -MIN_INT % 10

        neg = False
        if x < 0:
            neg = True
            x = -x

        res = 0
        while x:
            digit = x % 10
            x = x // 10
            if neg:
                # python for positive number, '//' removes decimals,
                # but for negative number, it removes decimal then minus one.
                # e.g. -722 // 10 = -73
                # for just removing decimals, use int()
                if -res < int(MIN_INT/10) or (-res == int(MIN_INT/10) and digit > min_int_digit):
                    return 0
            else:
                if res > MAX_INT//10 or (res == MAX_INT//10 and digit > max_int_digit):
                    return 0
            res = res*10 + digit
        if neg:
            res = -res
        return res

x = -9463847412

sol = Solution()
print(sol.reverse(x))
