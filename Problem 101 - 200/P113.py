# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sub(self, r: TreeNode, sum: int, path, res) -> None:
            if not r:
                return
            path.append(r.val)
            if not r.left and not r.right and r.val == sum:
                res.append(path[:])
            self.sub(r.left, sum - r.val, path, res)
            self.sub(r.right, sum - r.val, path, res)
            path.pop()

    def pathSum(self, root: TreeNode, sum: int):
        res = []
        self.sub(root, sum, [], res)
        return res

t = TreeNode(5)
t.left = TreeNode(4)
t.right = TreeNode(8)
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7)
t.left.left.right = TreeNode(2)
t.right.left = TreeNode(13)
t.right.right = TreeNode(4)
t.right.right.left = TreeNode(5)
t.right.right.right = TreeNode(1)

sol = Solution()
print(sol.pathSum(t, 22))
