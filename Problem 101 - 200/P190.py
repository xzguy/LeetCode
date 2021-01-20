class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = bin(n)[2:]
        while len(n_bin) < 32:
            n_bin = "0" + n_bin
        res = 0
        for c in n_bin[::-1]:
            if c == "1":
                res = 2*res+1
            else:
                res = 2*res
        return res

    def reverseBits_1(self, n: int) -> int:
        res = 0
        power = 31
        while n > 0:
            res += (n%2) << power
            n = n >> 1
            power -= 1
        return res

sol = Solution()
print(sol.reverseBits(3221225471))