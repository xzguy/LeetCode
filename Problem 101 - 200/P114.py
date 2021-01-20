# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        if root.right and root.left:
            root_pre = root.left
            while root_pre.right:
                root_pre = root_pre.right
            root_pre.right = root.right
            root.right = root.left
            root.left = None
            return self.flatten(root.right)
        if root.left:
            root.right = root.left
            root.left = None 
        return self.flatten(root.right)
    
    # non-recursive one
    def flatten_1(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

    def main(self, root: TreeNode) -> TreeNode:
        cur = root
        self.flatten_1(cur)
        return root

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(5)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right.right = TreeNode(6)

sol = Solution()
head = sol.main(t)
print(head)