class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary_str = ""
        while N > 0:
            binary_str = str(N % 2) + binary_str
            N = N//2
        if not binary_str:
            binary_str = "0"
        res = 0
        for b in binary_str:
            if b == "1":
                res = res*2
            else:
                res = res*2 + 1
        return res

    # since N and its complement adds to 1,1,...,1
    def bitwiseComplement_1(self, N: int) -> int:
        all_ones = 1
        while N > all_ones:
            all_ones = 2*all_ones + 1
        return all_ones - N