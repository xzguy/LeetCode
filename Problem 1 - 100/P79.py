class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        board_row = len(board)
        board_col = len(board[0])

        # sub-function to deal with one letter in 'word'
        def one_letter(r: int, c: int, word_p: int, path: [[int]]) -> bool:
            if word_p == len(word):
                return True
            ans = False
            # up
            if r > 0:
                if board[r-1][c] == word[word_p] and [r-1, c] not in path:
                    path.append([r, c])
                    ans = ans or one_letter(r-1, c, word_p+1, path)
                    path.pop()
            # down
            if r< board_row-1:
                if board[r+1][c] == word[word_p] and [r+1, c] not in path:
                    path.append([r, c])
                    ans = ans or one_letter(r+1, c, word_p+1, path)
                    path.pop()
            # left
            if c > 0:
                if board[r][c-1] == word[word_p] and [r, c-1] not in path:
                    path.append([r, c])
                    ans = ans or one_letter(r, c-1, word_p+1, path)
                    path.pop()
            # right
            if c < board_col-1:
                if board[r][c+1] == word[word_p] and [r, c+1] not in path:
                    path.append([r, c])
                    ans = ans or one_letter(r, c+1, word_p+1, path)
                    path.pop()
            return ans

        for r in range(board_row):
            for c in range(board_col):
                if board[r][c] == word[0] and one_letter(r, c, 1, []):
                    return True
        return False

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]]

sol = Solution()
print(sol.exist(board, "ABCCED"))
print(sol.exist(board, "SEE"))
print(sol.exist(board, "ABCB"))
