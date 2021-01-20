class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        board = [[0]* n for _ in range(n)]
        
        def bt(board: [[int]], row: int, n: int) -> None:
            if row == n:
                self.count += 1
                return
            else:
                for col in range(n):
                    if isValid(board, row, col, n):
                        board[row][col] = 1
                        bt(board, row+1, n)
                        board[row][col] = 0

        def isValid(board: [[int]], row: int, col: int, n: int) -> bool:
            for r in range(row):
                for c in range(n):
                    if board[r][c] == 1 and (c == col or
                                            c + r == col + row or
                                            c - r == col - row):
                        return False
            return True

        bt(board, 0, n)
        return self.count

sol = Solution()
print(sol.totalNQueens(5))