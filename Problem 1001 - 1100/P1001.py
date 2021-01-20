import collections

class Solution:
    def gridIllumination(self, N: int, lamps: [[int]], queries: [[int]]) -> [int]:
        res = []
        for query in queries:
            res.append(self.query_with_lamps(lamps, query))
            self.turn_off_lamps(query, lamps, N)
        return res
            
    def turn_off_lamps(self, lamp: [int], lamps: [[int]], N: int) -> None:
        row, col = lamp[0], lamp[1]
        for r in [row-1, row, row+1]:
            for c in [col-1, col, col+1]:
                if 0 <= r < N and 0 <= c < N and [r, c] in lamps:
                    lamps.remove([r, c])

    def query_with_lamps(self, lamps: [[int]], query: [int]) -> int:
        for lamp in lamps:
            if lamp[0] == query[0] or lamp[1] == query[1] or\
                abs(lamp[0] - query[0]) == abs(lamp[1] - query[1]):
                return 1
        return 0

    # use counter for more efficiency, same logic
    def gridIllumination_1(self, N: int, lamps: [[int]], queries: [[int]]) -> [int]:
        # list is not harhable, tuple is hashable.
        light_set = {(x, y) for x, y in lamps}
        horizontal = collections.Counter(x for x, y in lamps)
        vertical = collections.Counter(y for x, y in lamps)
        diag = collections.Counter(x - y for x, y in lamps)
        anti_diag = collections.Counter(x + y for x, y in lamps)

        res = []
        for x, y in queries:
            if horizontal[x] > 0 or vertical[y] > 0 or diag[x-y] > 0 or anti_diag[x+y] > 0:
                res.append(1)
            else:
                res.append(0)
            # 9 adjacent cells
            for dx in [-1, 0, 1]:
                for dy in [-1, 0 , 1]:
                    i, j = x+dx, y+dy
                    if (i, j) in light_set:
                        light_set.remove((i, j))
                        horizontal[i] -= 1
                        vertical[j] -= 1
                        diag[i-j] -= 1
                        anti_diag[i+j] -= 1

        return res

sol = Solution()
N = 5
lamps = [[0,0],[4,4]]
queries = [[1,1],[1,0]]
print(sol.gridIllumination_1(N, lamps, queries))