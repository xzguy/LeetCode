# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        lft = self.maxDepth(root.left)
        rght = self.maxDepth(root.right)
        if lft - rght > 1 or rght - lft > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, r: TreeNode) -> int:
        if not r:
            return 0
        lvl = 0
        queue = [r]
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                tmp = queue.pop(0)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            lvl += 1
        return lvl

    # store the intermediate tree max depth value in dictionary
    def isBalanced_1(self, root: TreeNode) -> bool:
        dict_maxDepth = {}

        def sub(r: TreeNode) -> bool:
            if not r:
                return True
            if r.left not in dict_maxDepth:
                lft = self.maxDepth(r.left)
                dict_maxDepth[r.left] = lft
            else:
                lft = dict_maxDepth[r.left]
            if r.right not in dict_maxDepth:
                rght = self.maxDepth(r.right)
                dict_maxDepth[r.right] = rght
            else:
                rght = dict_maxDepth[r.right]
            if lft - rght > 1 or rght - lft > 1:
                return False
            return sub(r.left) and sub(r.right)

        return sub(root)

    # recursive both on tree and max depth
    def isBalanced_2(self, root: TreeNode) -> bool:

        def sub(r: TreeNode) -> (bool, int):
            if not r:
                return (True, 0)
            lft = sub(r.left)
            rght = sub(r.right)
            isB = True
            if lft[1] - rght[1] > 1 or rght[1] - lft[1] > 1:
                isB = False
            depth = max(lft[1], rght[1]) + 1
            return (isB and lft[0] and rght[0], depth)
            
        return sub(root)[0]


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
#t.right.left = TreeNode(3)
t.left.left = TreeNode(3)
t.left.right = TreeNode(3)
t.left.left.left = TreeNode(4)
t.left.left.right = TreeNode(4)

sol = Solution()
print(sol.isBalanced_1(t))