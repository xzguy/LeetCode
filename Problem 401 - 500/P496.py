class Solution:
    '''
    This is the same as get the next greater element of
    nums2, then scan nums1
    '''
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        if not nums2:
            return []
        # get next greater element for nums2
        next_greater = [-1] * len(nums2)
        stack = [0]
        for i in range(1, len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                next_greater[idx] = nums2[i]
            stack.append(i)
        
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            idx = nums2.index(nums1[i])
            res[i] = next_greater[idx]
        return res