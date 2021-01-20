class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        lt_len = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:lt_len+1], inorder[0:lt_len])
        root.right = self.buildTree(preorder[lt_len+1:], inorder[lt_len+1:])
        return root
    
    # instead of create new list, use pointers
    def buildTree_1(self, preorder: [int], inorder: [int]) -> TreeNode:

        def sub(po_start, po_end, io_start, io_end) -> TreeNode:
            if po_start == po_end:
                return None
            root_val = preorder[po_start]
            root = TreeNode(root_val)
            lt_len = inorder.index(root_val) - io_start
            root.left = sub(po_start+1, po_start+lt_len+1, io_start, io_start+lt_len)
            root.right = sub(po_start+lt_len+1, po_end, io_start+lt_len+1, io_end)
            return root
            
        return sub(0, len(preorder), 0, len(inorder))


sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = sol.buildTree_1(preorder, inorder)
print(root)