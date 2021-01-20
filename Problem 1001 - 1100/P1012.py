import math

class Solution:
    # brute force
    def numDupDigitsAtMostN(self, N: int) -> int:
        res = 0
        while N > 0:
            if self.isRepeatDigits(N):
                res += 1
            N -= 1
        return res

    def isRepeatDigits(self, N: int) -> bool:
        digit_set = set()
        while N > 0:
            if N % 10 in digit_set:
                return True
            digit_set.add(N%10)
            N //= 10
        return False

    '''
    For number of 10^N, it is easier to calculate the number of repeated digits.
    To directly count the number with repeated digits is difficult, it is better
    to count the complement: number without repeated digits.
    '''
    def ordered_combinatorials(self, base: int, size: int) -> int:
        res = 1
        for _ in range(size):
            res *= base
            base -= 1
        return res

    '''
    instead of count number of repeated digits, it is easier
    to count the number with distinct digit
    '''
    def numDupDigitsAtMostN_1(self, N: int) -> int:
        res = N
        digit_list = []
        while N > 0:
            digit_list.append(N%10)
            N //= 10
        digit_list.reverse()
        if len(digit_list) < 2:
            return 0
        # remove distinct-digit numbers below digit_list[0]-1,9,9,...,9 (inclusive)
        res -= (digit_list[0]-1) * self.ordered_combinatorials(9, len(digit_list)-1)
        # remove distinct-digit numbers below 1,0,0,...,0 (inclusive)
        for i in range(len(digit_list)-1):
            res -= 9 * self.ordered_combinatorials(9, i)
        # remove distinct-digit numbers above digit_list[0],0,0,...,0 (inclusive)
        digit_set = {digit_list[0]}
        for i in range(1, len(digit_list)):
            for j in range(digit_list[i]):
                if j in digit_set:
                    continue
                res -= self.ordered_combinatorials(10-len(digit_set)-1, len(digit_list)-len(digit_set)-1)
            if digit_list[i] in digit_set:
                break
            else:
                digit_set.add(digit_list[i])
        # if the original number has no repeated digits
        if len(digit_list) == len(digit_set):
            res -= 1
        return res

    def numDupDigitsAtMostN_2(self, N):
        L = map(int, str(N + 1))
        res, n = 0, len(L)

        def A(m, n):
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

        for i in range(1, n):
            res += 9 * A(9, i - 1)
        s = set()
        for i, x in enumerate(L):
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            if x in s:
                break
            s.add(x)
        return N - res