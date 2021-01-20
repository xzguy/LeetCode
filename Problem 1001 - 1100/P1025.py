class Solution:
    '''
    For Alice to start, it is easy to find
    N = 1, lose
    N = 2, win
    N = 3, lose
    N = 4, win
    N = 5, lose
    N = 6, win
    N = 7, lose
    N = 8, win
    N = 9, lose
    N = 10, win
    So far, for even N, it is win; for odd N, it is lose.
    If N is even, and because N-1 is lose, so Alice can choose x=1
    and then Bob will face N-1 which is lose. So Alice wins.
    If N is odd, because of 0 < x < N and N%x == 0, x is odd.
    So, no matter what x it is, N-x is even which means Bob will win.
    So Alice loses.
    To sum up, if N is even, win; otherwise lose.
    '''
    def divisorGame(self, N: int) -> bool:
        return N%2 == 0