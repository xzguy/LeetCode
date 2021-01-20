# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        
        def sub(root, p, q):
            if p.val <= root.val <= q.val:
                return root
            if p.val > root.val:
                return sub(root.right, p, q)
            if root.val > q.val:
                return sub(root.left, p, q)

        return sub(root, p, q)