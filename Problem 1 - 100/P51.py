def solveNQueens(n: int) -> [[str]]:
    # backtrack
    def bt(results: [[str]], board: [[str]], row: int) -> None:
        if row == n:
            results.append([''.join(r) for r in board])
            return
        for col in range(n):
            if isValid(board, row, col, n):
                board[row][col] = 'Q'
                bt(results, board, row+1)
                board[row][col] = "."

    # only checks the column and diagonal collision
    def isValid(board: [str], row: int, col: int, n: int) -> bool:
        for r in range(row):
            for c in range(n):
                if (board[r][c] == 'Q') and (c == col or
                                            r-c == row-col or
                                            r+c == row+col):
                    return False
        return True

    board = [["."] * n for _ in range(n)] 
    results = []
    bt(results, board, 0)

    return results

print(solveNQueens(4))