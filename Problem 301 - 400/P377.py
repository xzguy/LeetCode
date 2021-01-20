class Solution:
    # recursive method
    def combinationSum4(self, nums: [int], target: int) -> int:
        if target == 0:
            return 1
        res = 0
        for num in nums:
            if num <= target:
                res += self.combinationSum4(nums, target-num)
        return res

    # dp memo
    def combinationSum4_1(self, nums: [int], target: int) -> int:

        def sub(target: int, memo: dict) -> int:
            if target == 0:
                return 1
            if target not in memo:
                res = 0
                for num in nums:
                    if num <= target:
                        res += sub(target - num, memo) 
                memo[target] = res
            return memo[target]

        return sub(target, {})

    # dp bottom-up
    def combinationSum4_2(self, nums: [int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for t in range(1, target+1):
            res = 0
            for num in nums:
                if num <= t:
                    res += dp[t-num]
            dp[t] = res
        return dp[-1]