class Solution:
    # dp, dp[i] = [length of longest increasing subsequence until i, number of these sequences]
    def findNumberOfLIS(self, nums: [int]) -> int:
        if not nums:
            return 0

        max_len = 1
        dp = []
        dp.append([1, 1])
        for i in range(1, len(nums)):
            # find the length of longest increasing subsequence until i
            cur_len = 1
            j = i-1
            while j >= 0:
                if nums[j] < nums[i]:
                    cur_len = max(cur_len, dp[j][0]+1)
                j -= 1
            max_len = max(max_len, cur_len)
            # find the number of these sequences
            cur_list_size = 0
            j = i-1
            while j >= 0:
                if dp[j][0] == cur_len-1 and nums[j] < nums[i]:
                    cur_list_size += dp[j][1]
                j -= 1
            if cur_list_size == 0:
                cur_list_size = 1
            
            dp.append([cur_len, cur_list_size])

        num_longest = 0
        for i in range(len(dp)):
            if dp[i][0] == max_len:
                num_longest += dp[i][1]
        return num_longest

nums = [2,2,2,2,2]
nums = [1,3,5,4,7]
nums = [1,2,4,3,5,4,7,2]
sol = Solution()
print(sol.findNumberOfLIS(nums))