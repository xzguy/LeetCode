'''
    Given a set of distinct integers,
return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
'''
def subsets_bt(nums: [int]) -> [[int]]:
    def backtrack_v1(results: [[int]], temp_set: [int], start: int) -> None:
        results.append(temp_set)
        for i in range(start, len(nums)):     
            backtrack_v1(results, temp_set+[nums[i]], i+1)
    
    def backtrack_v2(results: [[int]], temp_set: [int], start: int) -> None:
        results.append(temp_set.copy())
        for i in range(start, len(nums)):
            temp_set.append(nums[i])
            backtrack_v2(results, temp_set, i+1)
            temp_set.pop()
    
    result_subsets = []
    backtrack_v2(result_subsets, [], 0)
    return result_subsets

def subsets_iterate_v1(nums: [int]) -> [[int]]:
        res = [[]]
        for n in nums:
            temp = [c.copy() for c in res]
            for i in temp: i.append(n)
            res += temp
        return res

def subsets_iterate_v2(nums: [int]) -> [[int]]:
    res = [[]]
    for n in nums:
        res += [item+[n] for item in res]
    return res

def subsets_bit_manipulation(nums: [int]) -> [[int]]:
    n = len(nums)
    p = 1 << n
    ans = [[] for _ in range(p)]
    for i in range(p):
        for j in range(n):
            if i >> j & 1:  #i & 1 << j:
                ans[i].append(nums[j])
    return ans

nums = [1, 2, 3]
print(subsets_bit_manipulation(nums))