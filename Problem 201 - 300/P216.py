class Solution:
    def combinationSum3(self, k: int, n: int) -> [[int]]:
        if n < 1 or n > 45:
            return []
        
        # recursive and backtrack
        def sub(k: int, n: int, start: int, path: [int], res: [[]]) -> None:
            for i in range(start, 10):
                if i > n:
                    continue
                if k == 1:
                    if n == i:
                        res.append(path + [i])
                    else:
                        continue
                sub(k-1, n-i, i+1, path + [i], res)

        res = []
        sub(k, n, 1, [], res)
        return res

k = 3
n = 7
sol = Solution()
print(sol.combinationSum3(k, n))