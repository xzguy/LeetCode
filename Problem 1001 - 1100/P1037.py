class Solution:
    # the slope of two pairs are not equal
    def isBoomerang(self, points: [[int]]) -> bool:
        p_x = []
        p_y = []
        for x, y in points:
            p_x.append(x)
            p_y.append(y)
        # slope_1 = (p_y[0] - p_y[1])/(p_x[0] - p_x[1])
        # slope_2 = (p_y[2] - p_y[1])/(p_x[2] - p_x[1])
        return (p_y[0] - p_y[1]) * (p_x[2] - p_x[1]) != (p_x[0] - p_x[1]) * (p_y[2] - p_y[1])