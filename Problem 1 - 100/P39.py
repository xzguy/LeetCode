'''
Given a set of distinct numbers, and a target number,
find all unique combinations in that set whose sum is
target. The same number in the set can be used multiple
times. The number set and target are assumed to be positive.
'''
def combinationSum(candidates: [int], target: int) -> [[int]]:
    candidates.sort()
    def backtrack(results: [[int]], temp_combination: [int], target: int) -> None:
        if target == 0:
            results.append(temp_combination.copy())
        if target > 0:
            for n in candidates:
                if len(temp_combination) > 0 and n < temp_combination[-1]:
                    continue
                temp_combination.append(n)
                backtrack(results, temp_combination, target-n)
                temp_combination.pop()
        
    results_combination = []
    backtrack(results_combination, [], target)
    return results_combination

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))