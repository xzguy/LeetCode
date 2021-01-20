'''
Analysis:
    Use two traverses from both directions to simplify the analysis.
    In the traverse from left to right, for each position, get the
    maximum water height from left (image right boundary is always infinit.)
    Then traverse from right to left, do the same thing.
    Then for each postion i, we will have two values:
        from_left_height_max, from_right_heigh_max
    The water trapped for position i is:
        min(from_left_height_max, from_right_heigh_max) - height[i]
'''
def trap(height: [int]) -> int:
    N = len(height)
    left = [0] * N
    right = [0] * N
    # traverse from left to right
    cur_height = 0
    for i in range(N):
        if height[i] > cur_height:
            cur_height = height[i]
        left[i] = cur_height
    # traverse from right to left
    cur_height = 0
    for i in range(N-1, -1, -1):
        if height[i] > cur_height:
            cur_height = height[i]
        right[i] = cur_height
    # for each position, calculate the water trapped by
    # min(left[i], right[i]) - height[i]
    water = 0
    for i in range(N):
        water += min(left[i], right[i]) - height[i]
    return water

# another way, two traverses, from height i, only higher bar can trap the water
def trap_1(height: [int]) -> int:
    total_water = 0 
    trap_len = len(height)

    # first forward traverse
    cur_water = 0
    cur_high = 0
    for i in range(trap_len):
        # a new water trap with equal case
        if height[i] >= cur_high:
            cur_high = height[i]
            total_water += cur_water
            cur_water = 0
        else:
            cur_water += (cur_high - height[i])
    # second backward traverse
    cur_water = 0
    cur_high = 0
    for i in range(trap_len-1, -1, -1):
        # a new water trap without equal case
        if height[i] > cur_high:
            cur_high = height[i]
            total_water += cur_water
            cur_water = 0
        else:
            cur_water += (cur_high - height[i])
    return total_water

input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap([input]))