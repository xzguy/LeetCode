'''
    Given a collection of integers that may contain duplicates,
return all possible unique permutations.
'''

def permuteUnique_bt(nums: [int]) -> [[int]]:
    nums.sort()
    def backtrack(results: [[int]], temp_list: [int], used_list: [bool]) -> None:
        if (len(temp_list) == len(nums)):
            results.append(temp_list.copy())
        else:
            for i in range(len(nums)):
                if (used_list[i]): continue
                if ((i > 0 and nums[i] == nums[i-1]) and not used_list[i-1]): continue
                used_list[i] = True
                temp_list.append(nums[i])
                backtrack(results, temp_list, used_list)
                temp_list.pop()
                used_list[i] = False
    
    results_perm = []
    used_list = [False for _ in range(len(nums))]
    backtrack(results_perm, [], used_list)
    return results_perm

def permuteUnique_iterate(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in range(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n: break              # handles duplication
        ans = new_ans
    return ans

nums = [1, 1, 2]
print(permuteUnique_iterate(nums))