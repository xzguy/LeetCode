'''
Problem:
    Given an unsorted integer array, find the smallest
missing positive integer. The time complexity should be
O(n) and constant extra space.
Analysis:
    A very important observation is for input array with
length N, the first missing positive number must be in
range [1, N+1]. Also all numbers in the array which is 0
or negative or over N+1 should be ignored. Thus another array
with length N+1 can store while traversing the input array.
'''

def firstMissingPositive(nums: [int]) -> int:
    num_len = len(nums)
    record = [0 for _ in range(num_len+1)]

    for i in range(num_len):
        if nums[i] <= 0 or nums[i] > num_len+1:
            continue
        record[nums[i]-1] = i+1         # i+1 can make sure 0 is default empty
    for j in range(num_len+1):
        if record[j] == 0:
            return j + 1
    return -1           # default wrong answer

nums = [5,6,7,10,12,11,8,1,2,4,3]
print(firstMissingPositive(nums))