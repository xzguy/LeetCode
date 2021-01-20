class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # iterative
    def inorderTraversal(self, root: TreeNode) -> [int]:
        stack = []
        cur = root
        res = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    # recursive
    def inorderTraversal_1(self, root: TreeNode) -> [int]:
        res = []

        def sub(root: TreeNode, res: list) -> None:
            if not root:
                return
            sub(root.left, res)
            res.append(root.val)
            sub(root.right, res)
        
        sub(root, res)
        return res