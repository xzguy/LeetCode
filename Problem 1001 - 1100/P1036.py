class Solution:
    def isEscapePossible(self, blocked: [[int]], source: [int], target: [int]) -> bool:
        grid = [[0 for _ in range(10**6)] for _ in range(10**6)]
        stack = [(source[0], source[1])]
        while stack:
            x, y = stack.pop()
            if 0 <= x < 10**6 and 0 <= y < 10**6 and grid[x][y] == 0 and [x,y] not in blocked:
                grid[x][y] = 1
                stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
        return grid[target[0]][target[1]] == 1

    # the key point in this problem is the limited length of blocked <= 200
    # the maximum blocked area is 199 * (199 + 1) / 2 = 19900
    # instead of using grid of 10^6, only store the visited coordinates.
    def isEscapePossible_1(self, blocked: [[int]], source: [int], target: [int]) -> bool:
        blocked = set(map(tuple, blocked))

        '''
        In leetcode test case 31, the target and source should not be
        in the blocked. But it happens. So the following two lines
        of code can make the submission passed, but it should not be
        necessary.
        '''
        # if tuple(target) in blocked:
        #     blocked.remove(tuple(target))

        max_area = ((len(blocked)-1) * len(blocked))//2

        def dfs(source: [int], target: [int]) -> bool:
            stack = [(source[0], source[1])]
            visited = set()
            while stack:
                x, y = stack.pop()
                if len(visited) > max_area or [x, y] == target:
                    return True
                if 0 <= x < 10**6 and 0 <= y < 10**6 and (x,y) not in visited and (x,y) not in blocked:
                    visited.add((x, y))
                    stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
            return False

        return dfs(source, target) and dfs(target, source)

blocked = [[5,20],[10,10],[15,10],[10,30],[15,30],[20,30]]
source = [10,20]
target = [20,30]
sol = Solution()
print(sol.isEscapePossible_1(blocked, source, target))