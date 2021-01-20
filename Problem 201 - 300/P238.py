class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        prod = 1
        cnt_zero = 0
        for n in nums:
            if n != 0:
                prod *= n
            else:
                cnt_zero += 1
        res = [prod] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                if cnt_zero == 0:
                    res[i] //= nums[i]
                else:
                    res[i] = 0
            else:
                if cnt_zero > 1:
                    res[i] = 0
        return res