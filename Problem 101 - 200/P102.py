import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        res = []
        queue = []
        if not root:
            return []
        cur_lvl = 0
        queue.append((cur_lvl, root))
        while queue:
            tmp_pair = queue.pop(0)
            cur_lvl = tmp_pair[0]
            cur_node = tmp_pair[1]
            if len(res)-1 < cur_lvl:
                res.append([cur_node.val])
            else:
                res[cur_lvl].append(cur_node.val)
            if cur_node.left:
                queue.append((cur_lvl+1, cur_node.left))
            if cur_node.right:
                queue.append((cur_lvl+1, cur_node.right))
        return res

    # bfs
    def levelOrder_1(self, root: TreeNode) -> [[int]]:
        res = []
        if not root:
            return []
        queue = collections.deque([root])
        while queue:
            q_len = len(queue)
            cur_lvl = []
            for _ in range(q_len):
                node = queue.popleft()
                cur_lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_lvl)
        return res

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

sol = Solution()
print(sol.levelOrder_1(t))