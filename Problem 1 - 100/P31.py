'''
solution: two layer loops from the bottom
    from the end iterate forward, compare the current number with every number after
    if found current number is less than any one after,
    switch these two and sort the numbers after the index of former current number
'''
def nextPermutation_two_loop(nums: [int]) -> None:
    num_len = len(nums)
    if num_len == 0: return None
    if num_len <= 2: return nums.reverse()
    
    # more than two numbers in the list
    for i in range(num_len-1, -1, -1):
        for j in range(num_len-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[i+1:] = list(reversed(nums[i+1:]))
                return
    nums.reverse()
    return

# this algorithm can be improved with binary search for j
def nextPermutation_one_loop(nums: [int]) -> None:
    num_len = len(nums)
    if num_len == 0: return None
    if num_len <= 2: return nums.reverse()
    
    # more than two numbers in the list
    for i in range(num_len-2, -1, -1):
        if nums[i] < nums[i+1]:
            for j in range(num_len-1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i+1:] = list(reversed(nums[i+1:]))
                    return
    nums.reverse()
    return

nums = [1,3,2]
nextPermutation_one_loop(nums)
print(nums)