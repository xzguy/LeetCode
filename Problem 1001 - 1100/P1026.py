# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # this method compares the current node with its
    # all ancestors.
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def sub(root: TreeNode, V: int, ancestor: [int]) -> int:
            if not root:
                return 0
            for node in ancestor:
                V = max(V, abs(node.val - root.val))
            ancestor.append(root)
            return max(V, sub(root.left, V, ancestor[:]), sub(root.right, V, ancestor[:]))
        
        return sub(root, 0, [])

    # this method only compares the current node
    # with its ancestors' maximum and minimum.
    def maxAncestorDiff_1(self, root: TreeNode) -> int:
        max_diff = 0

        def sub(root: TreeNode, cur_max: int, cur_min: int) -> None:
            nonlocal max_diff
            if not root:
                return
            max_diff = max(max_diff, abs(root.val - cur_max), abs(root.val - cur_min))
            cur_max = max(cur_max, root.val)
            cur_min = min(cur_min, root.val)
            sub(root.left, cur_max, cur_min)
            sub(root.right, cur_max, cur_min)

        sub(root, root.val, root.val)
        return max_diff

    # another way to maintain the maximum and minimum of
    # every ancestor-offspring path
    def maxAncestorDiff_2(self, root: TreeNode) -> int:
        if not root:
            return 0

        def sub(root: TreeNode, cur_max: int, cur_min: int) -> int:
            if not root:
                return cur_max - cur_min
            cur_max = max(cur_max, root.val)
            cur_min = min(cur_min, root.val)
            left = sub(root.left, cur_max, cur_min)
            right = sub(root.right, cur_max, cur_min)
            return max(left, right)

        return sub(root, root.val, root.val)

t = TreeNode(8)

t.left = TreeNode(3)
t.right = TreeNode(10)

t.left.left = TreeNode(1)
t.left.right = TreeNode(6)
t.left.right.left = TreeNode(4)
t.left.right.right = TreeNode(7)

sol = Solution()
print(sol.maxAncestorDiff_2(t))

