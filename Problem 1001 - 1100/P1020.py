class Solution:
    def numEnclaves(self, A: [[int]]) -> int:
        if not A:
            return 0
        row = len(A)
        col = len(A[0])
        # for 4 boundaries, change 1 to 2, then explore
        for r_i in range(row):
            for c_i in range(col):
                if r_i in [0, row-1] or c_i in [0, col-1]:
                    if A[r_i][c_i] == 1:
                        A[r_i][c_i] = 2
                        stack = [(r_i, c_i)]
                        while stack:
                            node = stack.pop()
                            r, c = node[0], node[1]
                            # upper
                            if r-1 >= 0 and A[r-1][c] == 1:
                                A[r-1][c] = 2
                                stack.append((r-1, c))
                            # lower
                            if r+1 < row and A[r+1][c] == 1:
                                A[r+1][c] = 2
                                stack.append((r+1, c))
                            # left
                            if c-1 >= 0 and A[r][c-1] == 1:
                                A[r][c-1] = 2
                                stack.append((r, c-1))
                            # right
                            if c+1 < col and A[r][c+1] == 1:
                                A[r][c+1] = 2
                                stack.append((r, c+1))
        res = 0
        for r in range(row):
            for c in range(col):
                if A[r][c] == 1:
                    res += 1
        return res

    # same solution, another programming way
    def numEnclaves_1(self, A: [[int]]) -> int:
        if not A:
            return 0
        row = len(A)
        col = len(A[0])
        # for 4 boundaries, change 1 to 2, then explore
        for r_i in range(row):
            for c_i in range(col):
                if r_i in [0, row-1] or c_i in [0, col-1]:
                    if A[r_i][c_i] == 1:
                        stack = [(r_i, c_i)]
                        while stack:
                            node = stack.pop()
                            r, c = node[0], node[1]
                            if 0 <= r < row and 0 <= c < col and A[r][c] == 1:
                                A[r][c] = 2
                                stack.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
        res = 0
        for r in range(row):
            for c in range(col):
                if A[r][c] == 1:
                    res += 1
        return res
    
input = [[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
sol = Solution()
print(sol.numEnclaves(input))