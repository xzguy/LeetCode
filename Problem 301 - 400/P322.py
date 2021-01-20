class Solution:
    # BFS
    def coinChange(self, coins: [int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = set(coins)
        to_check = {amount}
        cnt = 0
        while to_check:
            cnt += 1
            temp = set()
            for x in to_check:
                for y in coins:
                    if x == y:
                        return cnt
                    if x > y:
                        temp.add(x-y)
            to_check = temp
        return -1

    # dp
    def coinChange_1(self, coins: [int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]]+1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

    # dp, simplified code
    def coinChange_2(self, coins: [int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        # reverse the two loops in the above method,
        # to avoid coins[j] > i
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i - coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1

coins = [474,83,404,3]
amount = 264
sol = Solution()
print(sol.coinChange_1(coins, amount))