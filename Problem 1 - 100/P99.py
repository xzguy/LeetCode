class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # use Morris traverse, find the two distorted tree Nodes,
    # and only swap their values
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        pre_node = None
        cur = root
        err_node_l = []
        while cur:
            chk_node = None
            if not cur.left:
                chk_node = cur
                cur = cur.right
            else:
                v_pre = cur.left
                while v_pre.right and v_pre.right != cur:     # here both '!=' and 'is not' are good
                    v_pre = v_pre.right

                if not v_pre.right:
                    v_pre.right = cur
                    cur = cur.left
                else:
                    v_pre.right = None
                    chk_node = cur
                    cur = cur.right
            
            if chk_node:
                if pre_node and pre_node.val > chk_node.val:
                    err_node_l.append(pre_node)
                    err_node_l.append(chk_node)
                pre_node = chk_node

        err_node_l[0].val, err_node_l[-1].val = err_node_l[-1].val, err_node_l[0].val

    # iterative in-order traverse
    def recoverTree_1(self, root: TreeNode) -> None:
        cur = root
        prev = TreeNode(float('-inf'))
        stack = []
        err_node_l = []

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev.val > cur.val:
                err_node_l.append(prev)
                err_node_l.append(cur)
            prev = cur
            cur = cur.right
        err_node_l[0].val, err_node_l[-1].val = err_node_l[-1].val, err_node_l[0].val


tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.right.left = TreeNode(2)
#tree.right.right = TreeNode(5)

sol = Solution()
sol.recoverTree(tree)