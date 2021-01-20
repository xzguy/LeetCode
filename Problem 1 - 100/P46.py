'''
    Given a set of distinct integers,
return all possible permutations.
'''
def permute_bt(nums: [int]) -> [[int]]:
    def backtrack(results: [[int]], temp_list: [int]) -> None:
        if (len(temp_list) == len(nums)):
            results.append(temp_list)
        else:
            for i in range(len(nums)):
                if (nums[i] in temp_list): continue
                backtrack(results, temp_list + [nums[i]])
    
    results_perm = []
    backtrack(results_perm, [])
    return results_perm

def permute_iterate(nums: [int]) -> [[int]]:
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms

nums = [1, 2, 3]
print(permute_iterate(nums))