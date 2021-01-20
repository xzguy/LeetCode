class Solution:
    '''
    N * (N-1) // (N-2) = 
    [(N-2) * (N-1) + 2 * (N-1)] // (n-2)
    N-1 + 2 * [(N-1) // (N-2)] = 
    N + 1 if (N-2) > 2
    N + 2 if (N-2) == 1 or 2, (it can be divisible by 2 * (N-1))
    '''
    def clumsy(self, N: int) -> int:
        if N == 1:
            return 1
        if N == 2:
            return 2 * 1
        if N == 3:
            return 3 * 2 // 1 
        if N == 4:
            return 4 * 3 // 2 + 1
        res = N+1
        N -= 3
        while N > 5:
            N -= 4
        if N == 1:
            return res + 1
        if N == 2:
            return res + 2 - 1
        if N == 3:
            return res + 3 - 2 * 1
        if N == 4:
            return res + 4 - 3 * 2 // 1
        if N == 5:
            return res + 5 - 4 * 3 // 2 + 1
