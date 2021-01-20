class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
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
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = list(reversed(res[i]))
        return res

    # if tree is large, reverse is expensive, try to avoid it.
    def zigzagLevelOrder_1(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        lvl = 0
        while queue:
            tmp = []
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if lvl % 2 == 0:
                res.append(tmp)
            else:
                res.append(list(reversed(tmp)))
            lvl += 1
        return res

t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.left.left = TreeNode(15)
t.right.right = TreeNode(7)

sol = Solution()
print(sol.zigzagLevelOrder_1(t))