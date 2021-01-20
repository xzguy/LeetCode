class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSym_sub(root.left, root.right)
        
    def isSym_sub(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSym_sub(p.left, q.right) \
                and self.isSym_sub(p.right, q.left)
        if not p and not q:
            return True
        return False

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
#t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right.left = TreeNode(4)
#t.right.right = TreeNode(3)


sol = Solution()
print(sol.isSymmetric(t))