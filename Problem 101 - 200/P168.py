class Solution:
    def convertToTitle(self, n: int) -> str:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n > 0:
            residue = n % 26
            if residue == 0:
                res = alpha[-1] + res
                n = n//26 - 1
            else:
                res = alpha[residue-1] + res
                n //= 26
        return res

    def convertToTitle_1(self, n: int) -> str:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ""
        while n > 0:
            n -= 1
            res = alpha[n%26] + res
            n //= 26
        return res

sol = Solution()
print(sol.convertToTitle(701))