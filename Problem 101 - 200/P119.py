class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        pre = []
        for i in range(rowIndex + 1):
            cur = [1] * (i+1)
            for j in range(1, i):
                cur[j] = pre[j-1] + pre[j]
            pre = cur
        return cur

    def getRow_1(self, rowIndex: int) -> [int]:
        if rowIndex < 0:
            return []
        pre = [1]
        for i in range(rowIndex):
            cur = [1] * (i//2 + 1)
            for j in range(1, i//2 + 1):
                cur[j] = pre[j-1] + pre[j]
            if i % 2 == 1:
                cur = cur + [2*pre[i//2]] + list(reversed(cur))
            else:
                cur = cur + list(reversed(cur))
            pre = cur
        return pre

sol = Solution()
print(sol.getRow_1(5))
