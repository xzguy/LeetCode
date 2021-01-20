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