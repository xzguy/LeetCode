def threeSumClosest(nums: [int], target: int) -> int:
    nums.sort()

    total_best = sum(nums[0:3])
    diff_min = abs(total_best - target)

    for i in range(len(nums)-2):
        j, k = i+1, len(nums)-1

        while (j < k):
            total = nums[i] + nums[j] + nums[k]
            diff = abs(total - target)
            if diff < diff_min:
                diff_min = diff
                total_best = total
            
            if total < target:
                j += 1
            elif total > target:
                k -= 1
            else:
                return total
    return total_best 

nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))