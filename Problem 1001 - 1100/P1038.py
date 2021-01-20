# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        cur = root
        prev_val = 0
        # reverse inorder DFS
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                prev_val += cur.val
                cur.val = prev_val
                cur = cur.left
        return root