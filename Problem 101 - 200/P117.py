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

    # recursive, traverse order is the key
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        if root.left and root.right:
            root.left.next = root.right
        if root.next:
            if root.right:
                pre = root.right
            elif root.left:
                pre = root.left
            else:
                pre = None
            if pre:
                nxt = None
                cur = root
                while cur.next and not nxt:
                    if cur.next.left:
                        nxt = cur.next.left
                    elif cur.next.right:
                        nxt = cur.next.right
                    else:
                        nxt = None
                    cur = cur.next
            if pre and nxt:
                pre.next = nxt
        # The order of traverse matters.
        # traverse from right to left
        self.connect(root.right)
        self.connect(root.left)
        return root
    
    # iterative level by level without queue
    def connect_3(self, root: Node) -> Node:
        if not root:
            return None
        l_most = root
        while l_most.left or l_most.right or l_most.next:
            if not l_most.left and not l_most.right:
                l_most = l_most.next
                continue
            cur = l_most
            while cur:
                if cur.left and cur.right:
                    cur.left.next = cur.right
                if cur.next:
                    pre = None
                    if cur.right:
                        pre = cur.right
                    elif cur.left:
                        pre = cur.left
                    else:
                        pre = None
                    if pre:
                        nxt = None
                        tmp = cur
                        while tmp.next and not nxt:
                            if tmp.next.left:
                                nxt = tmp.next.left
                            elif tmp.next.right:
                                nxt = tmp.next.right
                            else:
                                nxt = None
                            tmp = tmp.next
                        if pre and nxt:
                            pre.next = nxt
                cur = cur.next
            if l_most.left:
                l_most = l_most.left
            else:
                l_most = l_most.right
        return root


t = Node(0)
t.left = Node(2)
t.right = Node(4)
t.left.left = Node(1)
t.right.left = Node(3)
t.right.right = Node(-1)
t.left.left.left = Node(5)
t.left.left.right = Node(9)
t.right.left.right = Node(6)
t.right.right.right = Node(8)

sol = Solution()
res = sol.connect(t)
print(res)