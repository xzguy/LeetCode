# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        lvl = 1
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return lvl
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lvl += 1
        return lvl

t = TreeNode(3)
t.left = TreeNode(9)
t.left.left = TreeNode(1)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

sol = Solution()
print(sol.minDepth(t))