class Solution:
    def dieSimulator(self, n: int, rollMax: [int]) -> int:

        def sub(N: int, num: int, consec_roll: int, memo: dict) -> int:

            if N == 0:
                return 1
            if (N, num, consec_roll) not in memo:
                res = 0
                if rollMax[num] == consec_roll:
                    for i in range(6):
                        if i == num:
                            continue
                        res += sub(N-1, i, 1, memo)
                else:
                    for i in range(6):
                        if i == num:
                            res += sub(N-1, i, consec_roll+1, memo)
                        else:
                            res += sub(N-1, i, 1, memo)
                memo[N, num, consec_roll] = res
            return memo[N, num, consec_roll]

        res = 0
        memo = {}
        for i in range(6):
            res += sub(n-1, i, 1, memo)
        return res % (10**9 + 7)

n = 3
rollMax = [1,1,1,2,2,3]
sol = Solution()
print(sol.dieSimulator(n, rollMax))