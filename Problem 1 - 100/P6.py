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


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        str_rows = [""]*numRows
        row_idx = 0
        direction = 1
        for c in s:
            str_rows[row_idx] += c
            row_idx += direction
            if row_idx == numRows-1:
                direction = -1
            elif row_idx == 0:
                direction = 1
        return "".join(str_rows)

s = 'PAYPALISHIRING'
numRows = 2
sol = Solution()
print(sol.convert(s, numRows))