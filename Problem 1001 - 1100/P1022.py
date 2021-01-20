# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        def sub(root: TreeNode, above_value) -> int:
            cur_value = above_value*2 + root.val
            if root.left and root.right:
                return sub(root.left, cur_value) + sub(root.right, cur_value)
            elif root.left:
                return sub(root.left, cur_value)
            elif root.right:
                return sub(root.right, cur_value)
            else:
                return cur_value
        
        if not root:
            return 0
        return sub(root, 0)
        