class Solution:
    def grayCode_slow(self, n: int) -> [int]:
        if n == 0:
            return [0]
        binary = [0] * n
        gray_list_binary = []
        gray_list_binary.append(binary.copy())
        while len(gray_list_binary) < 2**n:
            for i in range(n):
                temp = binary.copy()
                temp[i] = (temp[i] + 1) % 2
                if temp not in gray_list_binary:
                    gray_list_binary.append(temp.copy())
                    binary = temp.copy()
                    break
        # convert binary to digital
        gray_list_digit = []
        for g in range(2**n):
            gray_digit = 0
            gray_binary = gray_list_binary[g]
            for i in range(n):
                if gray_binary[i] == 1:
                    gray_digit += 2**i
            gray_list_digit.append(gray_digit)
        return gray_list_digit

    def grayCode(self, n: int) -> [int]:
        gray_list_digit = [0]
        for i in range(n):
            gray_list_digit += [x + 2**i for x in reversed(gray_list_digit)]
        return gray_list_digit

sol = Solution()
print(sol.grayCode(3))