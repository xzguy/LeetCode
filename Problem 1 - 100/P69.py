def mySqrt(x):
    """
    : type x: int
    : rtype: int
    """
    if x == 0 or x == 1:
        return x

    res = x
    while res**2 > x:
        res = (res + x / res) // 2

    return int(res)

print(mySqrt(16))