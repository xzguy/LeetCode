def subsetsWithDup_bt(nums: [int]) -> [[int]]:
    nums.sort()

    def backtrack_v1(results: [[int]], temp_set: [int], start: int) -> None:
        results.append(temp_set.copy())
        for i in range(start, len(nums)):
            if (i > start and nums[i] == nums[i-1]): continue
            temp_set.append(nums[i])
            backtrack_v1(results, temp_set, i+1)
            temp_set.pop()

    def backtrack_v2(results: [[int]], temp_set: [int], start: int) -> None:
        results.append(temp_set.copy())
        for i in range(start, len(nums)):
            if (i > start and nums[i] == nums[i-1]): continue
            backtrack_v2(results, temp_set + [nums[i]], i+1)
    
    results_subset = []
    backtrack_v1(results_subset, [], 0)
    return results_subset

def subsetsWithDup_iterate_v1(nums: [int]) -> [[int]]:
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

def subsetsWithDup_iterate_v2(nums: [int]) -> [[int]]:
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res

nums = [1, 2, 2, 2]
print(subsetsWithDup_iterate_v2(nums))