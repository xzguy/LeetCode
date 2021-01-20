'''
Analysis:
    iterate forward. Greedy method.
'''
def jump(nums: [int]) -> int:
    if (len(nums)) < 2: return 0
    if (len(nums)) == 2: return 1
    
    num_step = 0
    p = 0
    while (p < len(nums)-1):
        longest_step = p + nums[p]
        num_step += 1
        if longest_step >= len(nums)-1:
            return num_step
        
        next_p = longest_step
        for i in range(1, nums[p]+1):
            if nums[p+i]+i+p > longest_step:
                longest_step = nums[p+i]+i+p
                next_p = p+i
        p = next_p
    return num_step

nums = [5,4,3,2,1,1,1]
print(jump(nums))