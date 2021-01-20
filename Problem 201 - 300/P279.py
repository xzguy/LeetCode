import math

class Solution:
    def is_square(self, n: int) -> bool:
        sqrt_int = int(math.sqrt(n))
        return sqrt_int**2 == n

    # dynamic programming way
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            if self.is_square(i):
                dp[i] = 1
                continue
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i], dp[i-j**2] + 1)
                j += 1
        return dp[-1]

    # bfs method which is faster than dynamic programming
    def numSquares_1(self, n: int) -> int:
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                y = 1
                while y**2 <= x:
                    if y**2 == x:
                        return cnt
                    temp.add(x - y**2)
                    y += 1
            toCheck = temp
        return cnt

    # mathematical way
    # Based on Lagrange's Four Square theorem, there 
    # are only 4 possible results: 1, 2, 3, 4.
    def numSquares_2(self, n: int) -> int:
        if self.is_square(n):
            return 1
        # The result is 4 if and only if n can be written in the 
        # form of 4^k*(8*m + 7). Please refer to 
        # Legendre's three-square theorem.
        while (n & 3) == 0: # n%4 == 0  
            n >>= 2
        if (n & 7) == 7: # n%8 == 7
            return 4
        i = 1
        while i**2 < n:
            if self.is_square(n-i**2):
                return 2
            i += 1
        return 3

sol = Solution()
print(sol.numSquares_1(12))