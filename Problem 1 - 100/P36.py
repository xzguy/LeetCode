'''
Analysis:
    define a sub-function to check validation of 9 elements.
Apply this function to all rows, columns and sub-squares.
'''
def isValidSudoku_v1(board: [[str]]) -> bool:
    
    # function to check no duplicate digit in one element(9 positions)
    def isValidElement(element: [str]) -> bool:
        digit_dict = set()
        for s in element:
            if s == ".": continue
            if s in digit_dict: 
                return False
            else:
                digit_dict.add(s)
        return True

    # check all rows
    for r in board:
        if not isValidElement(r):
            return False
    # check all columns
    for i in range(9):
        c = []
        for j in range(9):
            c.append(board[j][i])
        if not isValidElement(c):
            return False
    # check all sub-squares
    for c in range(9):
        for r in range(9):
            if c%3 == 0 and r%3 == 0:
                squ = []
                for c_x in range(3):
                    for r_x in range(3):
                        squ.append(board[r+r_x][c+c_x])
                if not isValidElement(squ):
                    return False
    return True

def isValidSudoku_v2(board: [[str]]) -> bool:
    rows = [{} for _ in range(9)]
    cols = [{} for _ in range(9)]
    squs = [{} for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != ".":
                num = int(num)
                squ_index = (r // 3)*3 + c//3

                rows[r][num] = rows[r].get(num, 0) + 1
                cols[c][num] = cols[c].get(num, 0) + 1
                squs[squ_index][num] = squs[squ_index].get(num, 0) + 1

                if rows[r][num] > 1 or cols[c][num] > 1 or squs[squ_index][num] > 1:
                    return False
    return True

sudoku1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

sudoku2 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku_v2(sudoku1))