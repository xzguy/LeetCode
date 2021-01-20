# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

'''
The key point is to avoid infinite loops
at the same time, copy next and random.
The program 133 is more generalized.
'''
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        # dictionary, key is original node, value is copy node
        m = {head: Node(head.val)}
        n = head
        while n:
            if n.next:
                if n.next not in m:
                    m[n.next] = Node(n.next.val)
                m[n].next = m[n.next]
            if n.random:
                if n.random not in m:
                    m[n.random] = Node(n.random.val)
                m[n].random = m[n.random]
            n = n.next
        return m[head]
