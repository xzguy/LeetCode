class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    beg = ListNode(0)
    prehead = beg
    prehead.next = head
    while prehead.next and prehead.next.next:
        a = prehead.next
        b = a.next
        prehead.next, b.next, a.next = b, a, b.next
        prehead = a
    return beg.next
    
