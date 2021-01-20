class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n%2 == 1:
                return False
            n = n >> 1
        return True

    def isPowerOfTwo_1(self, n: int) -> bool:
        pow = set()
        for i in range(32):
            pow.add(2**i)
        return n in pow