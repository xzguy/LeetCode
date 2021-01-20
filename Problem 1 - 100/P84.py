class Solution:
    def largestRectangleArea_bf1(self, heights: [int]) -> int:
        if not heights:
            return 0
        max_area = heights[0]
        for l in range(len(heights)):
            for r in range(l, len(heights)):
                area = (r - l + 1) * min(heights[l: r + 1])
                if area > max_area:
                    max_area = area
        return max_area

    def largestRectangleArea_bf2(self, heights: [int]) -> int:
        if not heights:
            return 0
        max_area = heights[0]
        for l in range(len(heights)):
            min_h = heights[l]
            for r in range(l, len(heights)):
                min_h = min(min_h, heights[r])
                max_area = max(max_area, (r - l + 1)*min_h)
        return max_area

    def largestRectangleArea_bf3(self, heights: [int]) -> int:
        if not heights:
            return 0
        max_area = heights[0]
        cur = 0
        while cur < len(heights):
            if heights[cur] == 0:
                cur += 1
                continue
            cur_min_height = heights[cur]
            cur_end = -1
            for i in range(cur+1, len(heights)):
                if heights[i] < cur_min_height:      
                    area = (i - cur)*cur_min_height
                    max_area = max(max_area, area)
                    cur_min_height = heights[i]
                    if heights[i] == 0:
                        cur_end = i
                        break
            if cur_end != -1:
                area = (cur_end - cur)*cur_min_height
            else:
                area = (len(heights) - cur)*cur_min_height
            max_area = max(max_area, area)
            cur += 1
        return max_area

    def largestRectangleArea(self, heights: [int]) -> int:
        if not heights:
            return 0

        leftmost = [None]*len(heights)
        rightmost = [None]*len(heights)
        leftmost[0] = 0
        rightmost[-1] = len(heights)-1

        if len(heights) < 2:
            return heights[0]

        # generate leftmost array, length at least 2
        for i in range(1, len(leftmost)):
            j = i-1
            while j >=0 and heights[i] <= heights[j]:
                j = leftmost[j]-1
            leftmost[i] = j+1

        # generate rightmost array, length at least 2
        for i in range(len(heights)-2, -1, -1):
            j = i+1
            while j < len(heights) and heights[i] <= heights[j]:
                j = rightmost[j]+1
            rightmost[i] = j-1

        max_area = heights[0]
        for i in range(len(heights)):
            max_area = max(max_area,
                           heights[i]*(rightmost[i]-leftmost[i]+1))
        return max_area


sol = Solution()
heights_list = [
    [4,2,0,3,2,4,3,4],      # 10
    [3,6,5,7,4,8,1,0],      # 20
    [2,1,5,6,2,3],          # 10
    [5,4,3,2,1],            # 9
    [2,1,2],                # 3
    [2,1,1,3],              # 4
    [10,9,8,7,6,5,4,3,2,1], # 30
    [2,4,6,8,10],           # 18
    [10,8,6,4,2],           # 18
    [9,2,3,5,4]             # 10
]
for i in range(len(heights_list)):
    ans_bf = sol.largestRectangleArea_bf2(heights_list[i])
    ans = sol.largestRectangleArea(heights_list[i])
    print(ans_bf, ',', ans)