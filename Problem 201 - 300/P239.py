import collections

class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        if not nums:
            return []
        if k == 1:
            return nums
        
        # monotonic queue
        MQ = collections.deque()
        res = []

        # travel first k numbers from left to right,
        # select a non-increasing subsequence and store their index
        for i in range(k):
            while MQ and nums[i] > nums[MQ[-1]]:
                MQ.pop()
            MQ.append(i)

        # now traverse from k to the end
        for i in range(k, len(nums)):
            res.append(nums[MQ[0]])

            # if the maximum will be out of window
            if MQ[0] < i-k+1:
                MQ.popleft()

            while MQ and nums[i] > nums[MQ[-1]]:
                MQ.pop()
            
            MQ.append(i)
        
        res.append(nums[MQ[0]])
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
sol = Solution()
print(sol.maxSlidingWindow(nums, k))