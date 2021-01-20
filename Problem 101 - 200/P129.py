# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def sub(root: TreeNode, parent_val: int) -> int:
            r_val = parent_val*10+root.val
            if root.left and root.right:
                return sub(root.left, r_val) + sub(root.right, r_val)
            elif root.left:
                return sub(root.left, r_val)
            elif root.right:
                return sub(root.right, r_val)
            else:
                return r_val

        if not root:
            return 0
        return sub(root, 0)

t = TreeNode(4)
t.left = TreeNode(9)
t.right = TreeNode(0)
t.left.left = TreeNode(5)
t.left.right = TreeNode(1)

sol = Solution()
print(sol.sumNumbers(t))