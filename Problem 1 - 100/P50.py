def myPow(x: float, n: int) -> float:
    if x == 0: return 1
    if n < 0:
        n = -n
        x = 1/x
    if x == 1: return 1
    
    element = x
    ans = 1
    while n > 0:
        if n%2 != 0:
            ans *= element
        n >>= 1
        element = element**2
    return ans

x = 2
n = -2

print(myPow(x, n))