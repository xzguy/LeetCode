def fourSum(nums: [int], target: int) -> [[int]]:
    def findNsum(nums, target, N, result, results):
        if len(nums) < N or N < 2: return
        
        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums)-1
            while (l < r):
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):
                if target < nums[0] * N or target > nums[-1] * N:
                    break
                if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                    findNsum(nums[i+1:], target-nums[i], N-1, result + [nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results


nums = [4,-9,-2,-2,-7,9,9,5,10,-10,4,5,2,-4,-2,4,-9,5]
target = -13
print(fourSum(nums, target))