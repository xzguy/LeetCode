import heapq

class Solution:
    # dynamic programming method
    # from the input, stations[:][0] is sorted (increment)
    # dp[i] means the furthest location we can go using i refueling stops.
    def minRefuelStops(self, target: int, startFuel: int, stations: [[int]]) -> int:
        dp = [0] * (len(stations)+1)
        dp[0] = startFuel
        for i, (location, capacity) in enumerate(stations):
            # loop direction matters
            for stop_num in range(i, -1, -1):
                if dp[stop_num] >= location:
                    dp[stop_num+1] = max(dp[stop_num+1], dp[stop_num] + capacity)
        
        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1
    
    # heap or priority queue method
    def minRefuelStops_1(self, target: int, startFuel: int, stations: [[int]]) -> int:
        # python heapq by default is min-heap, so
        # a max-heap is simulated using negative values
        pq = []
        stations.append((target, float('inf')))

        res = pre = 0
        tank = startFuel
        for location, capacity in stations:
            tank -= location - pre
            while pq and tank < 0: # must refuel in past
                tank += -heapq.heappop(pq)
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -capacity)
            pre = location
        return res

target = 1000
startFuel = 299
stations = [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]
sol = Solution()
print(sol.minRefuelStops(target, startFuel, stations))