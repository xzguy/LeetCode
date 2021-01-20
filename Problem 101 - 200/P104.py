class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        lvl = 0
        while queue:
            cur_lvl_len = len(queue)
            for _ in range(cur_lvl_len):
                tmp = queue.pop(0)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            lvl += 1
        return lvl

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.left.left = TreeNode(15)
t.right.right = TreeNode(7)

sol = Solution()
print(sol.maxDepth(t))