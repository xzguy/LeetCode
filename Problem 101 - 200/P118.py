class Solution:
    def generate(self, numRows: int) -> [[int]]:
        res = []
        for i in range(numRows):
            cur = [0] * (i+1)
            cur[0], cur[-1] = 1, 1
            for j in range(1, i):
                cur[j] = res[i-1][j-1] + res[i-1][j]
            res.append(cur)
        return res

    # since the Pascal's triangle is symmetric
    def generate_1(self, numRows: int) -> [[int]]:
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            cur = [0] * ((i+1)//2)
            cur[0] = 1
            for j in range(1, (i+1)//2):
                cur[j] = res[i-1][j-1] + res[i-1][j]
            if i % 2 == 0:
                cur = cur + [2*res[i-1][(i+1)//2-1]] + list(reversed(cur))
            else:
                cur = cur + list(reversed(cur))
            res.append(cur)
        return res

sol = Solution()
print(sol.generate_1(5))
        