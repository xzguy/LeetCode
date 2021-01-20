class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> [int]:
        [a, b, c] = sorted([a, b, c])
        # maximum moves occurs when both endpoint stones
        # moves towards to the middle by one each step
        max_moves = c-b-1 + b-a-1
        if b - a == 1:
            if c - b == 1:
                min_moves = 0
            else:
                min_moves = 1
        elif b - a == 2:
            min_moves = 1
        else:
            if c - b == 1 or c - b == 2:
                min_moves = 1
            else:
                min_moves = 2
        return [min_moves, max_moves]

