'''
Given a collection of numbers, and a target number,
find all unique combinations in that set whose sum is
target. The same number in the set can only be used
once. The number set and target are assumed to be positive.
'''
def combinationSum_one_use_bt(candidates: [int], target: int) -> [[int]]:
    candidates.sort()
    def backtrack(results: [[int]], temp_combination: [int], target: int, used_list: [bool]) -> None:
        if target == 0:
            results.append(temp_combination.copy())
        if target > 0:
            for i in range(len(candidates)):
                if used_list[i]:
                    continue
                if len(temp_combination) > 0 and candidates[i] < temp_combination[-1]:
                    continue
                if i > 0 and candidates[i] == candidates[i-1] and not used_list[i-1]:
                    continue
                temp_combination.append(candidates[i])
                used_list[i] = True
                backtrack(results, temp_combination, target-candidates[i], used_list)
                temp_combination.pop()
                used_list[i] = False
    
    def backtrack_compact(results: [[int]], temp_combination: [int], target: int, used_list: [bool]) -> None:
        if target == 0: results.append(temp_combination)
        if target > 0:
            for i in range(len(candidates)):
                if used_list[i]: continue
                if len(temp_combination) > 0 and candidates[i] < temp_combination[-1]: continue
                if i > 0 and candidates[i-1] == candidates[i] and not used_list[i-1]: continue
                used_list[i] = True
                backtrack_compact(results, temp_combination + [candidates[i]], target-candidates[i], used_list)
                used_list[i] = False

    results_combination = []
    used_list = [False for _ in range(len(candidates))]
    backtrack_compact(results_combination, [], target, used_list)
    return results_combination

def combinationSum_one_use_bt_better(candidates: [int], target: int) -> [[int]]:
    candidates.sort()
    def backtrack(results: [[int]], temp_combination: [int], target: int, start: int) -> None:
        if target == 0: results.append(temp_combination)
        if target > 0:
            for i in range(start, len(candidates)):
                # avoid the duplicate in current recursive only
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                backtrack(results, temp_combination + [candidates[i]], target-candidates[i], i+1)

    results_combination = []
    backtrack(results_combination, [], target, 0)
    return results_combination

candidates = [2,5,2,1,2]
target = 5
print(combinationSum_one_use_bt_better(candidates, target))