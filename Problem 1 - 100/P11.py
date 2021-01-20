def maxArea(height: [int]) -> int:
    if len(height) < 2:
        return -1

    max_water = 0
    i, j = 0, len(height)-1
    while (i < j):
        max_water = max(min(height[i], height[j]) * (j-i), max_water)
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return max_water

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))