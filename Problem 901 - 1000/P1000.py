class Solution:
    # greedy is wrong
    # for [6,4,4,6], this output is 42, but answer is 40
    def mergeStones_wrong(self, stones: [int], K: int) -> int:
        if (len(stones) - K) % (K-1) != 0:
            return -1

        cost = 0
        for _ in range((len(stones) - K) // (K-1)+1):
            merge_sum = sum(stones[:K])
            merge_idx = 0
            for i in range(1, len(stones)-K+1):
                if sum(stones[i:i+K]) < merge_sum:
                    merge_sum = sum(stones[i:i+K])
                    merge_idx = i
            cost += merge_sum
            stones = stones[:merge_idx] + [merge_sum] + stones[merge_idx+K:]
        return cost

    # dp function cache
    def mergeStones(self, stones: [int], K: int) -> int:
        n = len(stones)
        inf = float('inf')
        # accumulate the input array for easier slice sum
        accu = [0] * (n+1)
        for i in range(n):
            accu[i+1] = accu[i] + stones[i]
        
        import functools

        @functools.lru_cache(None)
        # means the cost for merging stones [i:j+1] into m piles
        def dp(i, j, m):
            if (j-i+1-m) % (K-1) != 0:
                return inf
            if i == j:
                if m == 1:
                    return 0
                else:
                    inf
            if m == 1:
                return dp(i, j, K) + accu[j+1] - accu[i]
            return min(dp(i, mid, 1) + dp(mid+1, j, m-1) for mid in range(i, j, K-1))
        
        res = dp(0, n-1, 1)
        return res if res < inf else -1

    # dp memo
    def mergeStones_1(self, stones: [int], K: int) -> int:
        def recursive(i, j, piles):
            if i == j and piles == 1:
                return 0
            if (i, j, piles) in dp:
                return dp[(i, j, piles)]
            if piles == 1:
                dp[(i,j,piles)] = recursive(i, j, K) + accu[j+1] - accu[i]
                return dp[(i,j,piles)]
            else:
                min_cost = float('inf')
                for k in range(i, j, K - 1):
                    min_cost = min(min_cost, recursive(i, k, 1) + recursive(k + 1, j, piles - 1))
                dp[(i, j, piles)] = min_cost
                return dp[(i, j, piles)]
        
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        accu = [0] * (n + 1)
        for i in range(n):
            accu[i + 1] = accu[i] + stones[i]
        dp = {}
        return recursive(0, n - 1, 1)

stones = [3,2,4,1]
K = 2
sol = Solution()
print(sol.mergeStones(stones, K))