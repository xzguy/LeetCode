# Standard library imports
import random

# Local application imports
import sys
sys.path.append('c:\\Users\\ShenChen\\Desktop\\Python_projects\\LeetCode')
import function_exec_time_compare as fetc

class Solution:
    # native
    def candy(self, ratings: [int]) -> int:
        peak = 0
        candy = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1]+1
                peak = i
            elif ratings[i] == ratings[i-1]:
                peak = i
            else:
                for j in range(i-1, peak-1, -1):
                    if candy[j] <= candy[j+1]:
                        candy[j] += 1
        return sum(candy)

    '''
    another method,
    for each number, find its candy number by search left and rigth for
    strictly decreasing number array.
    '''
    def candy_1(self, ratings: [int]) -> int:
        candy = [1 for _ in range(len(ratings))]
        for i in range(len(ratings)):
            left_more_candy = 0
            # search left
            for j in range(i-1, -1, -1):
                if ratings[j] < ratings[j+1]:
                    left_more_candy += 1
                else:
                    break
            right_more_candy = 0
            for j in range(i+1, len(ratings)):
                if ratings[j-1] > ratings[j]:
                    right_more_candy += 1
                else:
                    break
            candy[i] += max(left_more_candy, right_more_candy)
        return sum(candy)

    '''
    quick method, traverse from left to right and vise versa,
    then update with maximum of two traverses.
    '''
    def candy_2(self, ratings: [int]) -> int:
        left2right = [1] * len(ratings)
        right2left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            # left to rigth
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
            # rigth to left
            if ratings[len(ratings)-i-1] > ratings[len(ratings)-i]:
                right2left[len(ratings)-i-1] = right2left[len(ratings)-i]+1
        candy_sum = 0
        for i in range(len(ratings)):
            candy_sum += max(left2right[i], right2left[i])
        return candy_sum

    # quick method, one time traverse with constant space
    def count(self, n: int) -> int:
        return n*(n+1)//2

    def candy_3(self, ratings: [int]) -> int:
        if len(ratings) < 2:
            return len(ratings)
        candies = up = down = old_slope = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                new_slope = 1
            elif ratings[i] < ratings[i-1]:
                new_slope = -1
            else:
                new_slope = 0
            if (old_slope > 0 and new_slope == 0) or \
                (old_slope < 0 and new_slope >= 0):
                candies += (self.count(up) + self.count(down) + max(up, down))
                up = 0
                down = 0
            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1
            else:
                candies += 1
            old_slope = new_slope
        candies += (self.count(up) + self.count(down) + max(up, down) + 1)
        return candies

input = [8,8,9,2,1,0]
input = [8,9,5,3,4,2]
input = [1, 2, 3, 4, 5, 3, 2, 1, 2, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]
sol = Solution()
print(sol.candy_3(input))

# compare functions execution time
input = [random.randrange(8) for _ in range(100)]
input_func = random.shuffle
rep = 100
func_list = [sol.candy, sol.candy_1, sol.candy_2, sol.candy_3]
func_name_list = ["native", "double loop", "double traverse", "single traverse"]
fetc.compare_function_exec_time(input, input_func, rep, func_list, func_name_list)