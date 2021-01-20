class Solution:
    def queryString(self, S: str, N: int) -> bool:
        while N > 0:
            bin = self.decimal_2_binary_str(N)
            if not self.isSubstring(S, bin):
                return False
            N -= 1
        return True

    def isSubstring(self, s: str, sub: str) -> bool:
        sub_len = len(sub)
        for i in range(len(s) - sub_len + 1):
            if s[i:i+sub_len] == sub:
                return True
        return False

    def decimal_2_binary_str(self, N: int) -> str:
        res = ""
        while N > 0:
            res = str(N%2) + res
            N //= 2
        return res

    def queryString_1(self, S: str, N: int) -> bool:
        # function bin() has a prefix "0b" to represent it
        # is binary string
        return all(bin(i)[2:] in S for i in range(N, N//2, -1))


    '''
    Since the problem gives length of S is in [1, 1000]
    N is in [1, 10^9]
    It can be deduced that N is at most 2047.
    If N > 2047, then from 1024 to 2047, total 1024 different numbers(11 bits)
    but since S is at most 1000 bits long, it can have at most 990 substrings
    of length 11. So N <= 2047
    *** Further more ***
    For given 'S' and 'N', we say N <= 2^k-1, so N is at most k bits in binary,
    and N can have at most 2^(k-1) numbers of k bits.
    Also, S can have at most len(S)-k+1 number of substrings of length k.
    In the worse case, len(S)-k+1 number of substrings must present 2^(k-1)
    different numbers of k bits in binary. So
    len(S) - k + 1 >= 2^(k-1), or
    len(S) <= 2^(m-1) + m - 1, for smallest m,
    Then we can say, for a given S, N <= 2^m-1
    '''
    def queryString_2(self, S: str, N: int) -> bool:
        k = 1
        S_len = len(S)
        while S_len > 2**(k-1) + k - 1:
            k += 1
        if N > 2**k-1:
            return False
        return all(bin(i)[2:] in S for i in range(N, N//2, -1))

sol = Solution()
print(sol.queryString_1("1", 1))