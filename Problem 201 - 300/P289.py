'''
M * N,
1 live
0 dead
rule 1: less then 2 live neighbors, dies
rule 2: 2 or 3 live neighbors, lives
rule 3: more than 3 live neighbors, dies
rule 4: for a dead cell, if exactly 3 neighbors live, lives
'''

class Solution:
    def func(self, board: [[int]]):
        if not board:
            return

        row, col = len(board), len(board[0])
        next = [[None] * col for _ in range(row)]

        def get_neighboring_lives(r: int, c: int) -> int:
            live = 0
            # up
            if r-1 >= 0:
                live += board[r-1][c]
            # down
            if r+1 < row:
                live += board[r+1][c]
            # left
            if c-1 >= 0:
                live += board[r][c-1]
            # right
            if c+1 < col:
                live += board[r][c+1]
            # up left
            if r-1 >= 0 and c-1 >= 0:
                live += board[r-1][c-1]
            # up right
            if r-1 >= 0 and c+1 < col:
                live += board[r-1][c+1]
            # down left
            if r+1 < row and c-1 >= 0:
                live += board[r+1][c-1]
            # down right
            if r+1 < row and c+1 < col:
                live += board[r+1][c+1]
            return live

        for r in range(row):
            for c in range(col):
                live = get_neighboring_lives(r, c)
                if board[r][c] == 0:
                    if live == 3:
                        next[r][c] = 1
                    else:
                        next[r][c] = 0
                else:
                    if live < 2:
                        next[r][c] = 0
                    elif live < 4:
                        next[r][c] = 1
                    else:
                        next[r][c] = 0
        
        for r in range(row):
            for c in range(col):
                board[r][c] = next[r][c]
