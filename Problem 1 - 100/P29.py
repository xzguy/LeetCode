def mydivide(dividend: int, divisor: int) -> int:
    if divisor == 0:
        raise ValueError
    IntMax, IntMin = 2**31-1, -2**31
    positive = (dividend < 0) == (divisor < 0)
    dividend, divisor = abs(dividend), abs(divisor)

    if divisor == 1:
        if positive:
            return dividend if dividend < IntMax else IntMax
        else:
            return -dividend
    
    ans = 0
    while (dividend >= divisor):
        num_shift = 0
        temp = divisor
        while (dividend >= temp):
            temp <<= 1
            num_shift += 1
        ans += (1 << (num_shift-1))
        dividend -= (temp >> 1)

    if not positive:
        ans = -ans
    
    if ans > IntMax: ans = IntMax
    if ans < IntMin: ans = IntMin
    return ans


print(mydivide(29, -5))
print(mydivide(2147483648, 1))
print(mydivide(2, 5))
print(mydivide(-2147483648, -1))