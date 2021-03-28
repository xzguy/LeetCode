class Solution:
    def countSmaller(self, nums: [int]) -> [int]:
        '''
        The trivial method has complexity of O(n^2).
        This method uses Binary Indexed Tree.
        The time complexity is O(N*log(N))
        '''

        N = len(nums)
        res = []
        rank = {val: i+1 for i, val in enumerate(sorted(nums))}
        BITree = [0] * (N+1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                # (i & -i) gives the least significant bit
                # i += (i & -i)
                i = (i | (i-1)) + 1

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                # i -= (i & -i)
                i = i & (i-1)
            return s

        for x in reversed(nums):
            res.append(getSum(rank[x] - 1))
            update(rank[x])
        return res[::-1]

sol = Solution()
nums = [5, 2, 6, 1]
print(sol.countSmaller(nums))

