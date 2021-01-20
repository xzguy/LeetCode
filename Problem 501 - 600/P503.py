class Solution:
    '''
    To overcome the circular array, append [:-1] at the end
    '''
    def nextGreaterElements(self, nums: [int]) -> [int]:
        A = nums + nums[:-1]
        if not A:
            return []
        stack = [0]
        res = [-1] * len(A)
        for i in range(1, len(A)):
            while stack and A[i] > A[stack[-1]]:
                idx = stack.pop()
                res[idx] = A[i]
            stack.append(i)
        return res[:len(nums)]

    # Or, use module travese twice
    def nextGreaterElements_1(self, nums: [int]) -> [int]:
        if not nums:
            return []
        stack = [0]
        res = [-1] * len(nums)
        for i in range(1, len(nums)*2-1):
            i = i % len(nums)
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)
        return res