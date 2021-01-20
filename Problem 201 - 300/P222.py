# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes_1(self, root: TreeNode) -> int:
        if not root:
            return 0

        # dfs
        res = 0
        stack = [root]
        while stack:
            node = stack.pop()
            res += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
        
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        # get the most left node of root left child
        left_left_lvl = 1
        node = root.left
        while node:
            left_left_lvl += 1
            node = node.left
        # get the most left node of root right child
        right_left_lvl = 1
        node = root.right
        while node:
            right_left_lvl += 1
            node = node.left
        # root left child is a perfect complete tree
        if left_left_lvl == right_left_lvl:
            return 2**(left_left_lvl-1) + self.countNodes(root.right)
        else: # root right child is a perfect complete tree
            return 2**(right_left_lvl-1) + self.countNodes(root.left)