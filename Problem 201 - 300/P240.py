class Solution:
    '''
    recursive, since in the matrix, the number matrix[i][j] is maximum
    inside square matrix[0~i][0~j]. So if target > matrix[i][j], target
    can not be in that square. Also the number matrix[i][j] is minimum
    inside square matrix[i~end][j~end], so if if target < matrix[i][j],
    target can not be in that square. Cutting off these two squares, the
    original square only has two smaller squares. Recursively solve it.
    '''
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False
        
        # bottom right x and y, up left x and y
        def sub(ul_x: int, ul_y: int, br_x: int, br_y:int) -> bool:
            if ul_x > br_x or ul_y > br_y:
                return False
            diag = 0
            while diag <= min(br_x - ul_x, br_y - ul_y):
                if matrix[ul_y + diag][ul_x + diag] == target:
                    return True
                if matrix[ul_y + diag][ul_x + diag] > target:
                    break
                diag += 1
            return sub(ul_x + diag, ul_y, br_x, ul_y + diag-1) or sub(ul_x, ul_y + diag, ul_x + diag-1, br_y)

        row, col = len(matrix), len(matrix[0])
        return sub(0, 0, col-1, row-1)

    '''
    Another beautiful solution is start from right top position.
    Then go down means increase, go left means decrease.
    '''
    def searchMatrix_1(self, matrix: [[int]], target: int) -> bool:
        if not matrix:
            return False
        row, col = len(matrix), len(matrix[0])
        r = 0
        c = col-1
        while r < row and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
        return False


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 14
sol = Solution()
print(sol.searchMatrix(matrix, target))