# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        
        def sub(root, path, res):
            if root.left:
                sub(root.left, path + str(root.val) + "->", res)
            if root.right:
                sub(root.right, path + str(root.val) + "->", res)
            if not root.left and not root.right:
                res.append(path + str(root.val))

        if not root:
            return []
        res = []
        sub(root, "", res)
        return res