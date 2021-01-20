class Solution:
    # since the input is array of integer, use greedy method.
    def maxProduct(self, nums: [int]) -> int:
        
        def maxProductNoZero(nums_no_zeros: [int]) -> int:
            neg_cnt = 0
            res = 1
            for n in nums_no_zeros:
                if n < 0:
                    neg_cnt += 1
                res *= n
            if neg_cnt % 2 == 1:
                # calculate the maximum product after first negative index
                first_neg_idx = 0
                while first_neg_idx < len(nums_no_zeros):
                    if nums_no_zeros[first_neg_idx] < 0:
                        break
                    first_neg_idx += 1
                if first_neg_idx == len(nums_no_zeros)-1:
                    first_neg_post = nums_no_zeros[-1]
                else:
                    first_neg_post = 1
                    for i in range(first_neg_idx+1, len(nums_no_zeros)):
                        first_neg_post *= nums_no_zeros[i]
                # calculate the maximum product before last negative index
                last_neg_idx = len(nums_no_zeros)-1
                while last_neg_idx >= 0:
                    if nums_no_zeros[last_neg_idx] < 0:
                        break
                    last_neg_idx -= 1
                if last_neg_idx == 0:
                    last_neg_pre = nums_no_zeros[0]
                else:
                    last_neg_pre = 1
                    for i in range(last_neg_idx):
                        last_neg_pre *= nums_no_zeros[i]
                # only need to compare [:last_neg_idx] and [first_neg_idx+1:]
                return max(first_neg_post, last_neg_pre)
            else:
                return res

        max_p = None
        start = end = 0
        start_nonzero = False
        while end < len(nums):
            if start_nonzero:
                if nums[end] == 0:
                    if max_p == None:
                        max_p = max(0, maxProductNoZero(nums[start:end]))
                    else:
                        max_p = max(max_p, maxProductNoZero(nums[start:end]))
                    start_nonzero = False
                else:
                    pass
            else:
                if nums[end] == 0:
                    pass
                else:
                    start_nonzero = True
                    start = end
            end += 1
        if start_nonzero:
            if max_p == None:
                max_p = maxProductNoZero(nums[start:end])
            else:
                max_p = max(max_p, maxProductNoZero(nums[start:end]))
        elif max_p == None:
            max_p = 0
        return max_p

    # one pass without dealing with zeros seperately
    def maxProduct_1(self, nums: [int]) -> int:
        res = cur_min = cur_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_min, cur_max = cur_max, cur_min
            
            cur_min = min(nums[i], nums[i]*cur_min)
            cur_max = max(nums[i], nums[i]*cur_max)

            res = max(res, cur_min, cur_max)
        return res
             

sol = Solution()

input = [-2]
input = [-2,0,-1]
input = [0]
input = [-1,-1,0]
input = [-1,2,1,0,3,-2,4]
input = [2,3,-2,4]
print(sol.maxProduct_1(input))