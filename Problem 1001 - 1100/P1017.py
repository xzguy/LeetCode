class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        bin = []
        while N > 0:
            bin.append(N%2)
            N //= 2
        # binary number left side is least significant bit
        i = 1
        while i < len(bin):
            if bin[i] == 1:
                if i == len(bin)-1:
                    bin.append(1)
                else:
                    bin[i+1] += 1
                j = i+1
                while j < len(bin) and bin[j] == 2:
                    if j == len(bin)-1:                
                        bin.append(1)
                    else:
                        bin[j+1] += 1
                    bin[j] = 0
                    j += 1
            i += 2
        bin.reverse()
        return "".join(str(x) for x in bin)

    '''
    int(-3/2) will round to -1
    -3//2 will round to -2
    '''
    def baseNeg2_1(self, N: int) -> str:
        res = []
        while N:
            print(N)
            res.append(N%2)
            N = -(N//2)
        return "".join(map(str, res[::-1] or [0]))

sol = Solution()
print(sol.baseNeg2_1(31))