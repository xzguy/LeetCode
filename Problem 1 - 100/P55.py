'''
Analysis:
    iterate backward, if there is a '0', count it,
if there is non-zero, compare with the count. If 
the number is larger, set count to zero, otherwise
increment count by 1. After reaching the beginning, 
if count is zero, return True, otherwise False.
'''
def canJump(nums: [int]) -> bool:
    if len(nums) < 2:
        return True

    zero_count = 0
    for i in range(len(nums)-2, -1, -1):
        if nums[i] == 0:
            zero_count += 1
        elif zero_count > 0:
            if nums[i] > zero_count:
                zero_count = 0
            else:
                zero_count += 1
    return zero_count == 0

nums = [2,0,0]
print(canJump(nums))