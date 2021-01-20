def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if a == '':
        return b
    if b == '':
        return a
        
    if len(a) > len(b):
        input_long, input_short = a, b
    else:
        input_long, input_short = b, a
    
    len_diff = len(input_long) - len(input_short)
    result = str()
    carry = '0'

    for i in range(len(input_short)-1, -1, -1):
        if input_long[i + len_diff] == input_short[i]:
            result = carry + result
            if input_short[i] == '0':
                carry = '0'
            else:
                carry = '1'
        else:
            if carry == '1':
                result = '0' + result
            else:
                result = '1' + result
    
    for i in range(len_diff-1, -1, -1):
        if carry == '1':
            if input_long[i] == '1':
                result = '0' + result
            else:
                result = '1' + result
                carry = '0'
        else:
            result = input_long[i] + result
        
    if carry == '1':
        result = '1' + result

    return result

a = "101010"
b = "100"

print(addBinary(a, b))