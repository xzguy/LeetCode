class Solution:
    def findWords(self, board: [[str]], words: [str]) -> [str]:
        m, n = len(board), len(board[0])
        
        def has_word(word: str) -> bool:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        visited = set()
                        stack = [(0, i, j)]
                        while stack:
                            idx, x, y = stack.pop()
                            if idx == len(word):
                                return True
                            if 0 <= x < m and 0 <= y < n and board[x][y] == word[idx] and (x, y) not in visited:
                                visited.add((x, y))
                                stack.extend([(idx+1, x+1, y), (idx+1, x-1, y), (idx+1, x, y+1), (idx+1, x, y-1)])
            return False

        res = []
        for word in words:
            if has_word(word):
                res.append(word)

        return res