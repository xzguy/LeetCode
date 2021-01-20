# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        pass_root = self.tree_dep(root.left) + self.tree_dep(root.right)
        pass_left = self.diameterOfBinaryTree(root.left)
        pass_right = self.diameterOfBinaryTree(root.right)
        return max(pass_root, pass_left, pass_right)

    # BFS
    def tree_dep(self, root) -> int:
        if not root:
            return 0
        lvl = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl += 1
        return lvl

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
sol = Solution()
print(sol.diameterOfBinaryTree(t))