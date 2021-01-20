class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # fast check first
        if K%10 not in [1,3,7,9]:
            return -1
        digit = 1
        N = 1
        remainder = set()
        while N < K:
            N = N*10+1
            digit += 1
            
        while N%K not in remainder:
            if N%K == 0:
                return digit
            remainder.add(N%K)
            N %= K
            while N < K:
                N = N*10+1
                digit += 1

        return -1
        
K = 17
sol = Solution()
print(sol.smallestRepunitDivByK(K))

            