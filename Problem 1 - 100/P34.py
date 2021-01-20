'''
Analysis:
    binary tranverse the sorted number list twice.
In the first round, find beginning index of target,
in the second round, find ending index of target.
Maintaining two pointers is more complex.
'''
def searchRange(nums: [int], target: int) -> [int]:
    num_len = len(nums)
    if num_len == 0: return [-1, -1]
    begin = end = -1
    # first round of binary tranverse
    l, r = 0, num_len-1
    if nums[0] == target:
        begin = 0
    else:
        while (l < r-1):
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid
            else:
                r = mid
        if nums[r] == target:
            begin = r
        else:
            return [-1, -1]
    # second round of binary tranverse
    l, r = 0, num_len-1
    if nums[-1] == target:
        end = num_len-1
    else:
        while (l < r-1):
            mid = (l+r)//2
            if target < nums[mid]:
                r = mid
            else:
                l = mid
        if nums[l] == target:
            end = l
        else:
            return [-1, -1]
    return [begin, end]

nums = [5,7,7,8,8,8,8,9,10]
target = 8
print(searchRange(nums, target))