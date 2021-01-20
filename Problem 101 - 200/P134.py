class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        cost_abs = [g-c for (g,c) in zip(gas, cost)]
        if sum(cost_abs) < 0:
            return -1
        length = len(cost_abs)
        for start in range(length):
            tank = 0
            go = True
            for i in range(length):
                idx = (start+i) % length
                tank += cost_abs[idx]
                if tank < 0:
                    go = False
                    break
            if go:
                return start
        return -1

    '''
    The following two methods are much quicker,
    but they both are based on an assumption which I haven't proved now:
    'if sum(gas) >= sum(cost), then there must be solution'.
    Another information is that it is guaranteed that if there is solution,
    the solution is unique.
    '''
    def canCompleteCircuit_1(self, gas: [int], cost: [int]) -> int:
        cost_abs = [g-c for (g,c) in zip(gas, cost)]
        if sum(cost_abs) < 0:
            return -1
        length = len(cost_abs)
        end = 0
        start = length-1
        tank = cost_abs[start]
        while start > end:
            if tank >= 0:
                tank += cost_abs[end]
                end += 1
            else:
                start -= 1
                tank += cost_abs[start]
        if tank >= 0:
            return start
        else:
            return -1

    def canCompleteCircuit_2(self, gas: [int], cost: [int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        position = 0
        balance = 0
        for i in range(len(gas)):
            balance += (gas[i] - cost[i])
            if balance < 0:
                balance = 0
                position = i+1
        return position



gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
sol = Solution()
print(sol.canCompleteCircuit_2(gas, cost))