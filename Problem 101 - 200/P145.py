# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive
    def postorderTraversal(self, root: TreeNode) -> [int]:
        traversal = []

        def sub(root: TreeNode, traversal: [int]):
            if not root:
                return
            sub(root.left, traversal)
            sub(root.right, traversal)
            traversal.append(root.val)

        sub(root, traversal)
        return traversal

    # iterative
    def postorderTraversal_1(self, root: TreeNode) -> [int]:
        traversal = []
        stack = []
        last_visited = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if node.right and node.right != last_visited:
                    stack.append(node)
                    root = node.right
                else:
                    traversal.append(node.val)
                    last_visited = node
        return traversal


t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)

sol = Solution()
print(sol.postorderTraversal_1(t))