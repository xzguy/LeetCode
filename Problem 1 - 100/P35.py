def searchInsert_v1(nums: [int], target: int) -> int:
    num_len = len(nums)

    i, j = 0, num_len - 1
    if nums[0] >= target: return 0
    if nums[-1] < target: return j+1

    while (i < j):
        mid = i + (j-i+1)//2
        if nums[mid] < target:
            i = mid
        elif nums[mid] > target:
            j = mid - 1
        else:
            return mid
    return i+1
    
def searchInsert_v2(nums: [int], target: int) -> int:
    num_len = len(nums)
    if num_len == 0: return 0

    l, r = 0, num_len-1
    if target <= nums[0]: return 0
    if target == nums[-1]: return num_len-1
    if target > nums[-1]: return num_len

    while (l < r-1):
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid
        elif nums[mid] > target:
            r = mid
        else:
            return mid
    return r

nums = [1,3,5,6]
target = 7
print(searchInsert_v2(nums, target))