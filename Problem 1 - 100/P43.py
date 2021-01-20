'''
Analysis:
    To simplify the program, we can first reverse the
input string and then convert it into list. Then define
two sub-functions, summation of two list and multiplication
of one list with one integer. Use dictionary to store
calculated values.
'''
def multiply(num1: str, num2: str) -> str:
    # function for summation of two list of integers
    def list_summation(l_long: [int], l_short: [int]) -> [int]:
        ans = []
        extra = 0
        for i in range(len(l_short)):
            s = l_long[i] + l_short[i] + extra
            ans.append(s%10)
            extra = s // 10
        for i in range(len(l_short), len(l_long)):
            s = l_long[i] + extra
            ans.append(s%10)
            extra = s // 10
        if extra > 0:
            ans.append(extra)
        return ans
    # function for multiplication of one list with one integer
    def list_multiplication(l: [int], n: int) -> [int]:
        if n == 0: return [0]
        if n == 1: return l
        ans = []
        extra = 0
        for i in range(len(l)):
            p = n * l[i] + extra
            ans.append(p%10)
            extra = p // 10
        if extra > 0:
            ans.append(extra)
        return ans
        
    if (len(num1) >= len(num2)):
        list_l = [int(n) for n in (reversed(num1))]
        list_s = [int(n) for n in (reversed(num2))]
    else:
        list_l = [int(n) for n in (reversed(num2))]
        list_s = [int(n) for n in (reversed(num1))]
    
    production_dict = {}
    res = []
    for i in range(len(list_l)):
        if not production_dict.get(list_l[i]):
            p = list_multiplication(list_s, list_l[i])
            production_dict[list_l[i]] = p
        else:
            p = production_dict.get(list_l[i])
        if p != [0]:
            p = [0]*i + p
        if len(p) > len(res):
            res = list_summation(p, res)
        else:
            res = list_summation(res, p)
        
    return ''.join([str(n) for n in reversed(res)])

num1 = "17039"
num2 = "7218"
print(multiply(num1, num2))