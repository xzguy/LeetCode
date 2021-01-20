"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # BFS with queue
    def connect_2(self, root: Node) -> Node:
        if not root:
            return None
        queue = [root]
        while queue:
            q_len = len(queue)
            pre = None
            for _ in range(q_len):
                cur = queue.pop(0)
                if pre:
                    pre.next = cur
                pre = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

    # recursive
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        # the tree is a perfect tree
        if root.left:
            l = root.left
            r = root.right
            l.next = r
            while l.right:
                l = l.right
                r = r.left
                l.next = r
            self.connect(root.left)
            self.connect(root.right)
        return root

    # recursive another
    def connect_1(self, root: Node) -> Node:
        if not root:
            return None
        if root.left:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left
        self.connect_1(root.left)
        self.connect_1(root.right)
        return root
    
    # iterative level by level without queue
    def connect_3(self, root: Node) -> Node:
        if not root:
            return None
        l_most = root
        while l_most.left:
            cur = l_most
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            l_most = l_most.left
        return root

    # recursive with some duplicate next pointer assignment
    def connect_4(self, root: Node) -> Node:
        if root and root.left:
            self.connectNodes(root.left, root.right)
        return root
    
    def connectNodes(self, node1: Node, node2: Node) -> None:
        node1.next = node2
        if node1.left:
            self.connectNodes(node1.right, node2.left)
            self.connectNodes(node1.left, node1.right)
            self.connectNodes(node2.left, node2.right)

t = Node(1)
t.left = Node(2)
t.right = Node(3)
t.left.left = Node(4)
t.left.right = Node(5)
t.right.left = Node(6)
t.right.right = Node(7)

sol = Solution()
res = sol.connect_2(t)
print(res)