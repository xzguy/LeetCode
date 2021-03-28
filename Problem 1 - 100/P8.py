def myAtoi(s: str) -> int:
    ans = 0
    sign = 1
    IntMax = 2**31 - 1
    IntMin = -2**31
    num_digit = 0

    begin_number = False

    for i in range(len(s)):
        if (not begin_number) and (s[i] == ' '):
            continue
        if s[i].isdigit():
                begin_number = True
                ans = ans * 10 + int(s[i])
                num_digit += 1
                if num_digit >= 30:
                    if ans > IntMax: return IntMax
                    if sign == -1 and ans*sign < IntMin: return IntMin
        elif (not begin_number) and (s[i] in {'-', '+'}):
            begin_number = True
            if s[i] == '-': sign = -1
        else:
            break
    ans = ans * sign
    
    if ans > IntMax:
        return IntMax
    if ans < IntMin:
        return IntMin
    return ans


s = "    +1 1"
print(myAtoi(s))

class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        max_int_digit = MAX_INT % 10
        min_int_digit = -MIN_INT % 10

        res = 0
        sign = None
        read_digit = False
        for c in s:
            if c == ' ':
                if read_digit or sign != None:
                    break
            else: 
                if sign == None and c == '+' and not read_digit:
                    sign = '+'
                elif sign == None and c == '-' and not read_digit:
                    sign = '-'
                elif c in '0123456789':
                    num = int(c)
                    if sign == None or sign == '+':
                        if res > MAX_INT//10 or (res == MAX_INT//10 and num > max_int_digit):
                            return MAX_INT
                    if sign == '-':
                        if -res < int(MIN_INT/10) or (-res == int(MIN_INT/10) and num > min_int_digit):
                            return MIN_INT
                    res = res * 10 + num
                    read_digit = True
                else:
                    break
        if sign == '-':
            return -res
        return res

s = '-91283472332'
s = '00000-42a1234'
s = '  +  413'
sol = Solution()
print(sol.myAtoi(s))