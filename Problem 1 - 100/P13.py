def romanToInt(s: str) -> int:
    special_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
    'C': 100, 'D': 500, 'M': 1000}
    num = 0
    jump = False
    for i in range(len(s)):
        if jump == True:
            jump = False
            continue
        if i+1 < len(s) and s[i:i+2] in special_dict:
            num += special_dict[s[i:i+2]]
            jump = True
        else:
            num += roman_dict[s[i]]
    return num

s = 'MCMXCIV'
print(romanToInt(s))