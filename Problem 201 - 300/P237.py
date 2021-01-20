class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # shift the rest of linked list
    def deleteNode(self, node):
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
    
    # delete the next one instead and shift value
    def deleteNode_1(self, node):
        node.val = node.next.val
        node.next = node.next.next