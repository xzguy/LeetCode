'''
Analsysi:
    use a variable to represent the maximum sum that
contains the current number to traverse the list.
'''
def maxSubArray(nums: [int]) -> int:
    num_len = len(nums)
    if num_len == 0:
        raise ValueError

    if num_len == 1:
        return nums[0]

    largest_sum = nums[0]
    # the maximum sum that contains the current number
    cur_sum = nums[0]
    for i in range(1, num_len):
        if cur_sum > 0:
            cur_sum += nums[i]
        else:
            cur_sum = max(cur_sum, nums[i])
        largest_sum = max(largest_sum, cur_sum)
        
    return largest_sum

nums = [-2,-1]
print(maxSubArray(nums))