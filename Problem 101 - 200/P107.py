class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            q_len = len(queue)
            lvl_list = []
            for _ in range(q_len):
                node = queue.pop(0)
                lvl_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.insert(0, lvl_list)
        return res

    def levelOrderBottom_1(self, root: TreeNode) -> [[int]]:
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res)-1 < level:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.left.left = TreeNode(15)
t.right.right = TreeNode(7)

sol = Solution()
print(sol.levelOrderBottom_1(t))