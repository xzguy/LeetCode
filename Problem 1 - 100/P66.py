def plusOne(digits):
    """
    : type digits: [int]
    : rtype: [int]
    """
    for i in range(len(digits)):
        if digits[-1-i] != 9:
            digits[-1-i] += 1
            return digits
        else:
            digits[-1-i] = 0
    digits.insert(0, 1)
    return digits

print(plusOne([9, 9, 9, 9]))
    
