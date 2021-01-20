import math
import collections

'''
To determine a line, we need slope and intercept.
Let's use y-intercept, then we need to deal vertical lines seperately.
We use one dictionary for all lines.
The key is (slope, y-intercept), the values are list of points on this line.
If the line is vertical or slope is infinite, second item becomes x-intercept.

One key point of this problem is the accuracy of division.
use a pair of coprime numbers to represent division for absolute accuracy:
if A/B = slope and gcd(A, B) == 1, we use (A, B) to represent slope.
Same process is applied for intercept.
The input points coordinates have to be integers.
'''
class Solution:
    def maxPoints(self, points: [[int]]) -> int:
        if len(points) < 3:
            return len(points)

        line_dict = collections.defaultdict(list)
        # double loop for all pairs (i, j) of points
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                x_diff = points[i][0] - points[j][0]
                y_diff = points[i][1] - points[j][1]
                # vertical line, intercept is X-intercept
                if x_diff == 0:
                    slope = float('inf')
                    intercept = points[i][0]
                # not vertical line, intercept is Y-intercept
                else:
                    slope = self.get_coprime(y_diff, x_diff)
                    # Y-intercept should be y1 - slope * x1
                    # or (y1 - (y_diff / x_diff) * x1
                    # or (y1 * x_diff - y_diff * x1) / x_diff
                    intercept = self.get_coprime(points[i][1]*x_diff - y_diff*points[i][0], x_diff)
                # add points i and j into the dictionary with (slope, intercept) as key
                line_dict[(slope, intercept)].extend([i, j])
        # change the dictionary value into the number of unique points
        for line in line_dict:
            line_dict[line] = len(set(line_dict[line]))
        # return maximum value in the dictionary
        return line_dict[max(line_dict, key=lambda x: line_dict[x])]
    
    def get_coprime(self, a: int, b: int) -> (int, int):
        # denominator can not be zero, numerator can be zero
        # if numerator is zero, we do not care about denominator, so set it zero.
        if a == 0:
            return (0, 0)
        # since a/b == -a/-b, we need avoid it.
        if a < 0 and b < 0:
            a, b = -a, -b
        gcd = math.gcd(a, b)
        return (a // gcd, b // gcd)


input = [[1,1],[1,1],[1,1]]
input = [[1,1],[1,1],[0,0],[3,4],[4,5],[5,6],[7,8],[8,9]]
input = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
input = [[15,12],[9,10],[-16,3],[-15,15],[11,-10],[-5,20],[-3,-15],[-11,-8],[-8,-3],[3,6],[15,-14],[-16,-18],[-6,-8],[14,9],[-1,-7],[-1,-2],[3,11],[6,20],[10,-7],[0,14],[19,-18],[-10,-15],[-17,-1],[8,7],[20,-18],[-4,-9],[-9,16],[10,14],[-14,-15],[-2,-10],[-18,9],[7,-5],[-12,11],[-17,-6],[5,-17],[-2,-20],[15,-2],[-5,-16],[1,-20],[19,-12],[-14,-1],[18,10],[1,-20],[-15,19],[-18,13],[13,-3],[-16,-17],[1,0],[20,-18],[7,19],[1,-6],[-7,-11],[7,1],[-15,12],[-1,7],[-3,-13],[-11,2],[-17,-5],[-12,-14],[15,-3],[15,-11],[7,3],[19,7],[-15,19],[10,-14],[-14,5],[0,-1],[-12,-4],[4,18],[7,-3],[-5,-3],[1,-11],[1,-1],[2,16],[6,-6],[-17,9],[14,3],[-13,8],[-9,14],[-5,-1],[-18,-17],[9,-10],[19,19],[16,7],[3,7],[-18,-12],[-11,12],[-15,20],[-3,4],[-18,1],[13,17],[-16,-15],[-9,-9],[15,8],[19,-9],[9,-17]]
input = [[1,1],[2,2],[3,3]]
input = [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
input = [[0,0],[1,1],[0,0]]
sol = Solution()
print(sol.maxPoints(input))