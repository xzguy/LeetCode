class Solution:
    # this method is not fast enough for this problem
    def canPartition(self, nums: [int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False
        sum_set = {0}
        for num in nums:
            for s in sum_set:
                sum_set = sum_set | {s+num}
        return (num_sum//2) in sum_set

    # recursive method
    def canPartition_1(self, nums: [int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False

        # dfs
        def isSum(num_idx: int, sum_target: int) -> bool:
            if sum_target == 0:
                return True
            if num_idx == -1 or sum_target < 0:
                return False
            return isSum(num_idx-1, sum_target - nums[num_idx]) or \
                isSum(num_idx-1, sum_target)
        
        return isSum(len(nums)-1, num_sum//2)

    # dp memo
    def canPartition_2(self, nums: [int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False

        # dfs
        def isSum(num_idx: int, sum_target: int, memo: dict) -> bool:
            if sum_target == 0:
                return True
            if num_idx == -1 or sum_target < 0:
                return False
            if (num_idx, sum_target) not in memo:
                memo[num_idx, sum_target] = isSum(num_idx-1, sum_target, memo) or \
                    isSum(num_idx-1, sum_target - nums[num_idx], memo)
            return memo[num_idx, sum_target]
        
        return isSum(len(nums)-1, num_sum//2, {})

    # dp bottom-up
    # dp[i][j] is true if sum j can be formed by subset from array nums[:i+1]
    # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
    def canPartition_3(self, nums: [int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False

        dp = [[False] * (num_sum//2+1) for _ in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            for j in range(num_sum//2+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][-1]

import sys
sys.path.append('c:\\Users\\ShenChen\\Desktop\\Python_projects\\LeetCode')
import function_exec_time_compare as fetc

import random

input_len = 50

def generate_input(input, int_len = input_len) -> [int]:
    return [random.randint(1, 100) for _ in range(int_len)]

input = generate_input([])
rep = 10
sol = Solution()
func_list = [sol.canPartition, sol.canPartition_3]
func_name_list = ["set union", "table dp bottom-up"]

fetc.compare_function_exec_time(input, generate_input, rep, func_list, func_name_list)