# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive
    def preorderTraversal(self, root: TreeNode) -> [int]:
        traversal = []

        def sub(root: TreeNode, traversal: [int]):
            if not root:
                return
            traversal.append(root.val)
            sub(root.left, traversal)
            sub(root.right, traversal)

        sub(root, traversal)
        return traversal

    # iterative
    def preorderTraversal_1(self, root: TreeNode) -> [int]:
        if not root:
            return []

        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            traversal.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return traversal

t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)

sol = Solution()
print(sol.preorderTraversal_1(t))