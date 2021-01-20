import collections

class Solution:
    # use stack to track
    def solve(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        num_r = len(board)
        num_c = len(board[0])
        if num_c <= 2 or num_r <= 2:
            return
        
        borders_cor = []
        # up and bottom
        for i in range(num_c-1):
            borders_cor.append((0, i))
            borders_cor.append((num_r-1, num_c-1-i))
        # right and left
        for i in range(num_r-1):
            borders_cor.append((i, num_c-1))
            borders_cor.append((num_r-1-i, 0))

        for cor in borders_cor:
            cor_r = cor[0]
            cor_c = cor[1]
            if board[cor_r][cor_c] == 'O':
                stack = [(cor_r, cor_c)]
                while stack:
                    cur = stack.pop()
                    r = cur[0]
                    c = cur[1]
                    board[r][c] = 'A'
                    # upper neighbor
                    if r > 0 and board[r-1][c] == 'O':
                        stack.append((r-1, c))
                    # lower neighbor
                    if r < num_r-1 and board[r+1][c] == 'O':
                        stack.append((r+1, c))
                    # left neighbor
                    if c > 0 and board[r][c-1] == 'O':
                        stack.append((r, c-1))
                    # right neighbor
                    if c < num_c-1 and board[r][c+1] == 'O':
                        stack.append((r, c+1))
        
        # loop through the board, change 'O' to 'X', 'A' to 'O'
        for r in range(num_r):
            for c in range(num_c):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'A':
                    board[r][c] = 'O'

    # DFS for 4-nary tree (up, bottom, left and right)
    def solve_1(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        num_r = len(board)
        num_c = len(board[0])
        if num_c <= 2 or num_r <= 2:
            return
        
        def dfs(r: int, c: int) -> None:
            if r < 0 or r > num_r-1 or c < 0 or c > num_c-1 or board[r][c] != 'O':
                return
            board[r][c] = 'A'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        # first and last row
        for c in range(num_c):
            dfs(0, c)
            dfs(num_r-1, c)
        # right and left column
        for r in range(num_r):
            dfs(r, 0)
            dfs(r, num_c-1)

        # loop through the board, change 'O' to 'X', 'A' to 'O'
        for r in range(num_r):
            for c in range(num_c):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'A':
                    board[r][c] = 'O'

    # BFS, but very similar to the stack ones, better code
    def solve_2(self, board: [[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue =  collections.deque([])
        # get 4 borders 'O' into queue
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == 'O':
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
                board[r][c] = 'A'
                queue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

        # loop through the board, change 'O' to 'X', 'A' to 'O'
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'A':
                    board[r][c] = 'O'

input = [["O"]]

input = [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]

sol = Solution()
sol.solve_1(input)
print(input)
