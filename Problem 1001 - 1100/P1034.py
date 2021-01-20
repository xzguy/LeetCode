class Solution:
    def colorBorder(self, grid: [[int]], r0: int, c0: int, color: int) -> [[int]]:
        if not grid:
            return grid
        row = len(grid)
        col = len(grid[0])
        target_color = grid[r0][c0]
        stack = [(r0, c0)]
        # coloring the area with -1
        while stack:
            r, c = stack.pop()
            if 0 <= r < row and 0 <= c < col and grid[r][c] == target_color:
                # since all values in grid is >= 1
                grid[r][c] = -1
                stack.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
        # restore the inside area first
        for r in range(row):
            for c in range(col):
                if grid[r][c] == -1:
                    # not on the boundary of the grid
                    if r not in [0, row-1] and c not in [0, col-1]:
                        # 4 neighbors are -1 or target_color(it means just restored)
                        if grid[r-1][c] in [-1, target_color] and \
                            grid[r+1][c] in [-1, target_color] and \
                            grid[r][c-1] in [-1, target_color] and \
                            grid[r][c+1] in [-1, target_color]:
                            grid[r][c] = target_color
        # coloring border with input color
        for r in range(row):
            for c in range(col):
                if grid[r][c] == -1:
                    grid[r][c] = color
        return grid