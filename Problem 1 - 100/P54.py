# this solution is classical and symmetric
def spiralOrder_v1(matrix: [[int]]) -> [int]:
    if len(matrix) == 0: return []
    if len(matrix[0]) == 0: return []

    row = len(matrix)
    col = len(matrix[0])
    res = [None for _ in range(row * col)]
    p = 0

    layer = (min(row, col) + 1) // 2
    for i in range(layer):
        # traverse north
        for j in range(i, col-i-1):
            res[p] = (matrix[i][j])
            p += 1
        # only central one is left
        if i == col-i-1 and row == col:
            res[p] = (matrix[i][i])
            p += 1
        # traverse east
        for j in range(i, row-i-1):
            res[p] = (matrix[j][col-i-1])
            p += 1
        if i == row-i-1 and row < col:
            res[p] = (matrix[i][col-i-1])
            p += 1
        # traverse south
        if i != row-i-1:
            for j in range(col-1-i, i, -1):
                res[p] = (matrix[row-1-i][j])
                p += 1
        if i == col-i-1 and row > col:
            res[p] = (matrix[row-1-i][i])
            p += 1
        # traverse west
        if i != col-i-1:
            for j in range(row-1-i, i, -1):
                res[p] = (matrix[j][i])
                p += 1

    return res

# this solution is more elegent with respects
# of computerized data representation
def spiralOrder_v2(matrix: [[int]]) -> [int]:
    if len(matrix) == 0: return []
    if len(matrix[0]) == 0: return []

    up = left = 0
    down = len(matrix)
    right = len(matrix[0])

    ans = [None for _ in range(down * right)]
    ptr = 0

    while True:
        for i in range(left, right):
            ans[ptr] = matrix[up][i]
            ptr += 1
        up += 1
        if up >= down:
            break
        
        for i in range(up, down):
            ans[ptr] = matrix[i][right-1]
            ptr += 1
        right -= 1
        if right <= left:
            break
        
        for i in range(right-1, left-1, -1):
            ans[ptr] = matrix[down-1][i]
            ptr += 1
        down -= 1
        if down <= up: 
            break

        for i in range(down-1, up-1, -1):
            ans[ptr] = matrix[i][left]
            ptr += 1
        left += 1
        if left >= right:
            break

    return ans
    

# this solution is very concise python style one
def spiralOrder_v3(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder_v3([*zip(*matrix)][::-1])

matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(spiralOrder_v3(matrix))