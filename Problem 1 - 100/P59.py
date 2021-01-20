def generateMatrix(n: int) -> [[int]]:
    mat = [[None]*n for _ in range(n)]
    ptr = 1
    for layer in range(n // 2):
        # north
        for i in range(layer, n-layer-1, 1):
            mat[layer][i] = ptr
            ptr += 1
        # east
        for i in range(layer, n-layer-1, 1):
            mat[i][n-layer-1] = ptr
            ptr += 1
        # south
        for i in range(n-layer-1, layer, -1):
            mat[n-layer-1][i] = ptr
            ptr += 1
        # west
        for i in range(n-layer-1, layer, -1):
            mat[i][layer] = ptr
            ptr += 1

    if n % 2 == 1:
        mat[n//2][n//2] = ptr

    return mat

print(generateMatrix(3))