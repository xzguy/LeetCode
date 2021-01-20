class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1

        board = [[0] * N for _ in range(N)]
        board[r][c] = 1
        knight_moves = [[1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2]]

        for _ in range(K):
            new_board = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if board[i][j] > 0:
                        for x,y in knight_moves:
                            if 0 <= i+x < N and 0 <= j+y < N:
                                new_board[i+x][j+y] += board[i][j]
            board = new_board

        num_stay = 0
        for i in range(N):
            for j in range(N):
                num_stay += board[i][j]
        return num_stay / 8**K
