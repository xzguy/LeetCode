def ZigZagConvert(s: str, numRows: int) -> str:
    if numRows == 1: return s

    str_list = [""] * min(numRows, len(s))
    cur_row = 0
    going_down = False

    for c in s:
        str_list[cur_row] += c
        if (cur_row == 0 or cur_row == numRows - 1): going_down = not going_down
        if going_down:
            cur_row += 1
        else:
            cur_row -= 1
            
    result = ""
    for row_str in str_list:
        result += row_str
    return result
         

s = "PAYPALISHIRING"
print(ZigZagConvert(s, 3))
