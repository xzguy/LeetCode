class Solution:
    def twoCitySchedCost(self, costs: [[int]]) -> int:
        a_minus_b = [a-b for a, b in costs]
        a_minus_b.sort()
        # exclusive threshold for flying to city A
        fly_a_threshold = a_minus_b[len(a_minus_b)//2]
        cost = 0
        fly_b = 0
        for a, b in costs:
            if a-b < fly_a_threshold:
                cost += a
            elif a-b > fly_a_threshold:
                cost += b
                fly_b += 1
        for a, b in costs:
            if a-b == fly_a_threshold:
                if fly_b < len(costs)//2:
                    cost += b
                    fly_b += 1
                else:
                    cost += a
        return cost

    # simplied coding
    def twoCitySchedCost_1(self, costs: [[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0]-x[1])
        cost = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                cost += costs[i][0]
            else:
                cost += costs[i][1]
        return cost