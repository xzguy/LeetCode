class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for n in num_set:
            if n-1 not in num_set:
                cur_streak = 1
                cur_n = n
                while cur_n+1 in num_set:
                    cur_streak += 1
                    cur_n += 1
                longest_streak = max(longest_streak, cur_streak)
        return longest_streak

nums = [100, 4, 200, 1, 3, 2]
sol = Solution()
print(sol.longestConsecutive(nums))
