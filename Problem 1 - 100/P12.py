import math

def intToRoman_single(single_digit: int, num_digit: int) -> str:
    if num_digit == 1:
        unit, unit_5, unit_10 = 'I', 'V', 'X'
    elif num_digit == 2:
        unit, unit_5, unit_10 = 'X', 'L', 'C'
    elif num_digit == 3:
        unit, unit_5, unit_10 = 'C', 'D', 'M'
    elif num_digit == 4:
        unit, unit_5, unit_10 = 'M', '', ''
    else:
        raise ValueError

    if single_digit < 4:
        return unit * single_digit
    elif single_digit == 4:
        return unit + unit_5
    elif single_digit < 9:
        return unit_5 + unit*(single_digit-5)
    else:
        return unit + unit_10

def intToRoman(num: int) -> str:
    if num == 0:
        return ''
    num_digit = math.floor(math.log10(num)) + 1
    h_digit = num // (10**(num_digit-1))
    left_num = num - h_digit * (10**(num_digit-1))
    return intToRoman_single(h_digit, num_digit) + intToRoman(left_num) 

print(intToRoman(1994))
