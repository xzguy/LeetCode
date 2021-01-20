class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tail_0 = 0
        head_2 = len(nums)-1
        cur = 0

        while cur <= head_2:
            if nums[cur] == 2:
                while nums[head_2] == 2:
                    head_2 -= 1
                    if head_2 == cur:
                        break
                nums[cur], nums[head_2] = nums[head_2], nums[cur]
                head_2 -= 1
            if nums[cur] == 0:
                if cur > tail_0:
                    nums[cur], nums[tail_0] = nums[tail_0], nums[cur]
                tail_0 += 1
            cur += 1

        print(nums)

sol = Solution()
sol.sortColors([2, 0, 1])
