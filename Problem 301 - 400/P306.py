class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def sub(a: int, b: int, start_idx: int) -> bool:
            if start_idx == len(num):
                return False
            if a+b != 0 and num[start_idx] == '0':
                return False
            if a + b == int(num[start_idx:]):
                return True
            end_idx = start_idx + 1
            while end_idx < len(num):
                if a + b == int(num[start_idx:end_idx]):
                    break
                end_idx += 1
            if end_idx == len(num):
                return False
            return sub(b, a+b, end_idx)
            
        for i in range(1, len(num)+1):
            for j in range(i+1, len(num)+1):
                a = num[:i]
                b = num[i:j]
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                if sub(int(a), int(b), j):
                    return True
        return False

num = "121202436"
sol = Solution()
print(sol.isAdditiveNumber(num))