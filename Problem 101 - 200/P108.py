class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: [int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
    # instead of generating new list, use index
    def sortedArrayToBST_1(self, nums: [int]) -> TreeNode:

        def sub(start, end) -> TreeNode:
            if start >= end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = sub(start, mid)
            root.right = sub(mid+1, end)
            return root
            
        return sub(0, len(nums))

sol = Solution()
nums = [-10, -3, 0, 5, 9]
nums = [0, 1, 2, 3, 4, 5, 6]
t = sol.sortedArrayToBST_1(nums)
print(t)