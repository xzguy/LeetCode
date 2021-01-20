def climbStairs(n):
    """
    : type n: int
    : rtype: int
    """
    result_list = [1, 2]
    for i in range(2, n):
        result_list.append(result_list[i-1] + result_list[i-2])
    return result_list[n-1]

print(climbStairs(5))