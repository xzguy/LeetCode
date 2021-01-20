import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS, only store most right node
    def rightSideView(self, root: TreeNode) -> [int]:
        res = []
        queue = collections.deque()
        if not root:
            return []
        queue.append(root)
        while queue:
            q_len = len(queue)
            get_node = False
            for _ in range(q_len):
                node = queue.popleft()
                if not get_node:
                    res.append(node.val)
                    get_node = True
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return res

