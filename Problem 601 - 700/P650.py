class Solution:
    '''
    factorizing n, n = x1 * x2 * x3 * ... * xn, then
    the total number of steps is x1 + x2 + ... + xn
    this number is minimum when all xi is prime number, because
    for p,q >= 2; p*q >= p + q; because
    (p-1) * (q-1) >= 1
    '''
    def minSteps(self, n: int) -> int:
        res = 0
        # even factor: only 2
        while n > 1 and n % 2 == 0:
            res += 2
            n //= 2
        # odd factor
        divisor = 3
        while n > 2:
            # finally n equals divisor
            while n % divisor == 0:
                res += divisor
                n //= divisor
            divisor += 2
        return res

    # this is dynamic programming method,
    # indeed, it is very similar to the above maths solution
    def minSteps_1(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            # trivial upper bound
            dp[i] = i
            for j in range(i//2, 1, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[-1]