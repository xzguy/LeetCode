def countAndSay(n: int) -> str:
    if n == 1: return '1'

    count_say_dict = ['' for _ in range(n)]
    count_say_dict[0] = '1'
    for i in range(1, n):
        cur_num = count_say_dict[i-1][0]
        count = 1
        for j in range(1, len(count_say_dict[i-1])):
            if count_say_dict[i-1][j] == cur_num:
                count += 1
            else:
                count_say_dict[i] += (str(count)+cur_num)
                cur_num = count_say_dict[i-1][j]
                count = 1
        count_say_dict[i] += (str(count)+cur_num)

    return count_say_dict[n-1]

    
print(countAndSay(2))
