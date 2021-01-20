def reverse_int(x: int) -> int:
    int_max = 2**31 - 1
    int_min = -2**31
    if x > int_max or x < int_min: return 0

    ans = 0
    sign = 1
    if x < 0:
        sign = -1
        x = -x

    while (x > 0):
        digit = x % 10
        x = x // 10
        ans = ans * 10 + digit

    ans = ans * sign
    if ans > int_max or ans < int_min: return 0

    return ans

x = -12345667954

print(reverse_int(x))
