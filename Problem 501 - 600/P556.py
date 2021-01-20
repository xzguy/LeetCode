class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1
        digits = []
        while n > 0:
            digits.append(n%10)
            n //= 10
        digits = digits[::-1]

        i = len(digits)-2
        while i >= 0:
            if digits[i] < digits[i+1]:
                break
            i -= 1
        if i == -1:
            return -1
        # the digits[i-1:] is decreasing 
        # so find the digit just above digit[i] from right side
        j = len(digits)-1
        while j > i and digits[j] <= digits[i]:
            j -= 1

        digits[i], digits[j] = digits[j], digits[i]
        # after this switch, array digits[i+1:] is still decreasing
        # and the smallest number requires digits[i+1:] sorted increasing
        # so here, we can just reverse it.
        res = 0
        digits[i+1:] = reversed(digits[i+1:])
        for j in range(len(digits)):
            res = res*10 + digits[j]
        if res >= 2**31:
            return -1
        return res

n = 230241
sol = Solution()
print(sol.nextGreaterElement(n))