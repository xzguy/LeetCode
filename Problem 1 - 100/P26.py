def removeDuplicates(nums: [int]) -> int:
    if len(nums) < 2: return len(nums)
    
    start = 1
    end = len(nums) - 1
    while start <= end:
        if nums[start] == nums[start-1]:
            del nums[start]
            end -= 1
        else:
            start += 1

    return len(nums)
    

nums = [1,1]
print(removeDuplicates(nums))