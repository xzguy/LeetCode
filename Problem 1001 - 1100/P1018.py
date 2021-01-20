class Solution:
    def prefixesDivBy5(self, A: [int]) -> [bool]:
        num = 0
        res = []
        for a in A:
            num = 2*num + a
            if num % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res