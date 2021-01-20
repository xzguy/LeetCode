# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        left_max = right_max = through_root = float('-inf')
        if root.left:
            left_max = self.maxPathSum(root.left)
        if root.right:
            right_max = self.maxPathSum(root.right)
        through_root = root.val
        if self.dfs_post_order(root.left) > 0:
            through_root += self.dfs_post_order(root.left)
        if self.dfs_post_order(root.right) > 0:
            through_root += self.dfs_post_order(root.right)
        return max(left_max, right_max, through_root)

    # left, right, then node
    def dfs_post_order(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_max = self.dfs_post_order(root.left)
        right_max = self.dfs_post_order(root.right)
        child_max = max(left_max, right_max)
        if child_max > 0:
            return root.val + child_max
        else:
            return root.val

    # there are many duplicated calculation of child most
    def maxPathSum_1(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        def dfs_post_order_1(root: TreeNode) -> int:
            nonlocal max_sum
            if not root:
                return 0
            left_max = dfs_post_order_1(root.left)
            right_max = dfs_post_order_1(root.right)
            # max sum through root 
            through_root = root.val
            if left_max > 0:
                through_root += left_max
            if right_max > 0:
                through_root += right_max
            max_sum = max(max_sum, through_root)
            # max sum of one branch from root
            child_max = max(left_max, right_max)
            if child_max > 0:
                return root.val + child_max
            else:
                return root.val

        dfs_post_order_1(root)
        return max_sum


t = TreeNode(-10)
t.left = TreeNode(9)
t.right = TreeNode(20)
# t.left.left = TreeNode(-4)
# t.left.right = TreeNode(-5)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

sol = Solution()
print(sol.maxPathSum_1(t))
