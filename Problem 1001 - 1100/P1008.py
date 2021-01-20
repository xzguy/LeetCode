# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.treeFromPreorderInorder(preorder, inorder)

    def treeFromPreorderInorder(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder:
            return None
        root_val = preorder[0]
        left_len = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.treeFromPreorderInorder(preorder[1:1+left_len], inorder[0:left_len])
        root.right = self.treeFromPreorderInorder(preorder[1+left_len:], inorder[1+left_len:])
        return root
    
    def bstFromPreorder_1(self, preorder: [int]) -> TreeNode:
        inorder = sorted(preorder)
        
        # instead of string slicing, use two pointers
        def treeFromPreorderInorder_1(po_start: int, po_end:int, io_start: int, io_end: int) -> TreeNode:
            if po_start >= po_end:
                return None
            root_val = preorder[po_start]
            left_len = inorder.index(root_val) - io_start
            root = TreeNode(root_val)
            root.left = treeFromPreorderInorder_1(po_start+1, po_start+1+left_len, io_start, io_start+left_len)
            root.right = treeFromPreorderInorder_1(po_start+1+left_len, po_end, io_start+1+left_len, io_end)
            return root

        return treeFromPreorderInorder_1(0, len(preorder), 0, len(inorder))

    def bstFromPreorder_2(self, preorder: [int]):
        return self.buildTree(preorder[::-1], float('inf'))

    def buildTree(self, A, bound):
        if not A or A[-1] > bound: return None
        node = TreeNode(A.pop())
        node.left = self.buildTree(A, node.val)
        node.right = self.buildTree(A, bound)
        return node