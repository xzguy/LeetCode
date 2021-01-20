class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            num = res
        return num

    '''
    Module 9 is the key point here.
    The last digit left will be module 9.
    Decompose 10...00 into 9...99 + 1 to derive it.
    '''
    def addDigits_1(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9