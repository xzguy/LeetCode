class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n&1
            #res += (n%2)
            n = n >> 1
        return res
    
    # Simon Berkovich uses this method
    def hammingWeight_1(self, n: int) -> int:
        res = 0
        while n != 0:
            res += 1
            n = n&(n-1)
        return res
