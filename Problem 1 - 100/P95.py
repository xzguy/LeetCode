class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> []:
        if n == 0:
            return []

        def genTreeList(start: int, end: int) -> [TreeNode]:
            tree_l = []
            # leave's left and right are None, if there is no 'None'
            #   "for left in left_l:"
            # and
            #   "for right in right_l:"
            # will not execute
            if start > end:
                tree_l.append(None)
            for i in range(start, end+1):
                left_l = genTreeList(start, i-1)
                right_l = genTreeList(i+1, end)
                for left in left_l:
                    for right in right_l:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        tree_l.append(root)
            return tree_l
            
        return genTreeList(1, n)

sol = Solution()
tree_list = sol.generateTrees(2)