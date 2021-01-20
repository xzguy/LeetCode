class Solution:
    '''
    This method is wrong!! Because different orderings are counted.
    For example, amount = 5, coins = [1, 2, 5]
    1,2,2 and 2,1,2 are both counted, which is not required in this problem.
    
    To avoid this, we need to apply some restriction on the recursion:
        dp[i] = dp[i-coin_1] + dp[i-coin_2] + ... + dp[i-coin_N]
    N = len(coins)
    Think about a tree, for each node there are N children representing
    making up the sum with N possible coins first.
    We can add an ordering restriction on this tree to avoid the above problem.
    For root, it has N children, then for coin_N, it can have N children from 1 to N
    for coin_i, it can only have i children from 1 to i;
    for coin_1, it can only have 1 child which is itself.
    In this way, each tree node represents a unique sum decomposition.
    '''
    def change_wrong(self, amount: int, coins: [int]) -> int:
        if not coins:
            if amount == 0:
                return 1
            return 0
        # dp[i] means the number of ways to sum to i
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 :
                    dp[i] += dp[i-coin]
        return dp[-1]

    # correct method based on the above analysis
    def change(self, amount: int, coins: [int]) -> int:
        
        def sub(amount_left: int, coin_idx: int, memo: dict) -> int:
            # reach a summation in the tree
            if amount_left == 0:
                return 1
            # since coin value is always positive, no way to get the sum
            if amount_left < 0:
                return 0
            if (amount_left, coin_idx) not in memo:
                res = 0
                for i in range(coin_idx+1):
                    res += sub(amount_left-coins[i], i, memo)
                memo[amount_left, coin_idx] = res
            return memo[amount_left, coin_idx]
        
        return sub(amount, len(coins)-1, {})

    # dp, faster than the above recursive
    # the key point is to order the decomposition of sum
    # for any decomposition, make the coins appear in the same order in coins[].
    # Then, it is very natrual to think dp[i][j] is the number of
    # ways to reach the sum j with first i kinds of coins.
    # then dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]] (not use coins[i] + use it)
    def change_1(self, amount: int, coins: [int]) -> int:
        if amount == 0:
            return 1

        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        
        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j-coins[i-1] >= 0:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[-1][-1]

sol = Solution()
amount = 10
coins = [1, 2, 5]
print(sol.change_1(amount, coins))