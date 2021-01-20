'''
Analysis:
    binary tranverse number list twice. In the first round,
find the rotate pivot. In the second round, binary search
with the rotate pivot as the shift to make the original
array in ascending order.
'''
def search_v1(nums: [int], target: int) -> int:
    num_len = len(nums)
    if num_len == 0: return -1

    l, r = 0, num_len-1
    while (l < r-1):
        mid = (l+r) // 2
        if nums[l] > nums[mid]:
            r = mid
        else:
            l = mid
    # if rotate
    if nums[l] > nums[r]: shift = r
    # no rotate
    else: shift = 0
    l, r = 0, num_len-1
    if nums[(l+shift) % num_len] == target: return (l+shift) % num_len
    if nums[(r+shift) % num_len] == target: return (r+shift) % num_len
    while (l < r-1):
        mid = (l+r) // 2
        if target > nums[(mid+shift)%num_len]:
            l = mid
        elif target < nums[(mid+shift)%num_len]:
            r = mid
        else:
            return (mid+shift)%num_len
    return -1

'''
Analysis:
    first binary tranverse the number list to find rotate
pivot. Choose one from two parts of original number list
separated by the rotate pivot for binary search.
    This method is not necessary better than v1
'''
def search_v2(nums: [int], target: int) -> int:
    num_len = len(nums)
    if num_len == 0: return -1
    # rotate pivot is the smallest number in list
    l, r = 0, num_len-1
    while (l < r-1):
        mid = (l+r)//2
        if nums[mid] > nums[l]:
            l = mid
        else:
            r = mid
    if nums[l] > nums[r]: p = r
    else: p = 0
    # if target is inside later part of number list
    if p == 0:
        l, r = 0, num_len-1
    elif target <= nums[-1]:
        l, r = p, num_len-1
    else:
        l, r = 0, p-1
    if nums[l] == target: return l
    if nums[r] == target: return r
    while (l < r-1):
        mid = (l+r)//2
        if target < nums[mid]:
            r = mid
        elif target > nums[mid]:
            l = mid
        else:
            return mid
    return -1

nums = [4,5,6,7,0,1,2]
nums2 = [11,13, 15, 1]
nums3 = [3, 1]
target = 1

print(search_v2(nums3, target))