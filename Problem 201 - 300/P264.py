class Solution:
    Ugly = [1]
    '''
    The recursive relation in this problem is easy to notice.
    The key point is these kind of ugly numbers are very sparse, which
    means the way to calculate prime numbers are not appliable here.
    The first solution is not accepted in Leetcode, because each iteration
    only increment 'num' by 1
    '''
    def nthUglyNumber(self, n: int) -> int:
        if n <= len(self.Ugly):
            return self.Ugly[n-1]
        res = self.Ugly
        num = self.Ugly[-1] + 1
        while len(res) < n:
            while not((num % 2 == 0 and num//2 in res) or \
                (num % 3 == 0 and num//3 in res) or \
                (num % 5 == 0 and num//5 in res)):
                num += 1
            res.append(num)
            num += 1
        self.Ugly = res
        return res[-1]

    def nthUglyNumber_1(self, n: int) -> int:
        res = [1]
        idx_2 = idx_3 = idx_5 = 0
        while len(res) < n:
            i = min(res[idx_2]*2, res[idx_3]*3, res[idx_5]*5)
            if i == res[idx_2]*2:
                idx_2 += 1
            if i == res[idx_3]*3:
                idx_3 += 1
            if i == res[idx_5]*5:
                idx_5 += 1
            res.append(i)
        return res[-1]
        
n = 129
sol = Solution()
print(sol.nthUglyNumber_1(n))