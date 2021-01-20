class Solution:
    # recursive method, very slow
    def lastStoneWeightII(self, stones: [int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        res = float('inf')
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                stone_i = stones[i]
                stone_j = stones[j]
                stones.remove(stone_i)
                stones.remove(stone_j)
                stones.append(abs(stone_i - stone_j))
                res = min(res, self.lastStoneWeightII(stones))
                stones.remove(abs(stone_i - stone_j))
                stones.append(stone_i)
                stones.append(stone_j)
        return res

    # with memo, but the key needs to sort every time, so not fast
    def lastStoneWeightII_1(self, stones: [int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]

        def sub(stones: [int], memo: dict) -> int:
            stones_key = tuple(sorted(stones))
            if stones_key not in memo:
                if len(stones) == 1:
                    memo[stones_key] = stones[0]
                else:
                    res = float('inf')
                    for i in range(len(stones)):
                        for j in range(i+1, len(stones)):
                            stone_i = stones[i]
                            stone_j = stones[j]
                            stones.remove(stone_i)
                            stones.remove(stone_j)
                            stones.append(abs(stone_i - stone_j))
                            res = min(res, sub(stones, memo))
                            stones.remove(abs(stone_i - stone_j))
                            stones.append(stone_i)
                            stones.append(stone_j)
                    memo[stones_key] = res
            return memo[stones_key]

        return sub(stones, {})

    # knapsack problem, dp solution
    def lastStoneWeightII_2(self, stones: [int]) -> int:
        A = stones
        dp = {0}
        sumA = sum(A)
        for a in A:
            # for each possible weight before a,
            # add a, then union with the dp set
            dp |= {a + i for i in dp}
        return min(abs(sumA - i - i) for i in dp)

stones = [1,3,4,3,5,4]
sol = Solution()
print(sol.lastStoneWeightII_2(stones))