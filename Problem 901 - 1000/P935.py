class Solution:
    '''
    Convert the problem into a graph:
    0 -> (4, 6)
    1 -> (6, 8)
    2 -> (7, 9)
    3 -> (4, 8)
    4 -> (0, 3, 9)
    5 -> (None)
    6 -> (0, 1, 7)
    7 -> (2, 6)
    8 -> (1, 3)
    9 -> (2, 4)
    '''
    def knightDialer(self, n: int) -> int:
        dial = [1] * 10
        for _ in range(n-1):
            next_dial = [0] * 10
            next_dial[0] += dial[4] + dial[6]
            next_dial[1] += dial[6] + dial[8]
            next_dial[2] += dial[7] + dial[9]
            next_dial[3] += dial[4] + dial[8]
            next_dial[4] += dial[0] + dial[3] + dial[9]
            next_dial[6] += dial[0] + dial[1] + dial[7]
            next_dial[7] += dial[2] + dial[6]
            next_dial[8] += dial[1] + dial[3]
            next_dial[9] += dial[2] + dial[4]
            dial = next_dial
        return sum(dial) % (10**9 + 7)