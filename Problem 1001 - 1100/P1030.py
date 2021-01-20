class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> [[int]]:
        res = []
        for r in range(R):
            for c in range(C):
                res.append([r,c])
        return sorted(res, key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))