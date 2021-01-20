class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        if not inorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        lt_len = inorder.index(root_val)
        root.left = self.buildTree(inorder[0:lt_len], postorder[0:lt_len])
        root.right = self.buildTree(inorder[lt_len+1:], postorder[lt_len:-1])
        return root
    
    # instead of create new list, use pointers
    def buildTree_1(self, inorder: [int], postorder: [int]) -> TreeNode:

        def sub(io_start, io_end, po_start, po_end) -> TreeNode:
            if io_start == io_end:
                return None
            root_val = postorder[po_end-1]
            root = TreeNode(root_val)
            lt_len = inorder.index(root_val) - io_start
            root.left = sub(io_start, io_start+lt_len, po_start, po_start+lt_len)
            root.right = sub(io_start+lt_len+1, io_end, po_start+lt_len, po_end-1)
            return root
            
        return sub(0, len(inorder), 0, len(postorder)) 

sol = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = sol.buildTree_1(inorder, postorder)
print(root)