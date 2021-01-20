class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    prehead = ListNode(-1)
    head = prehead

    while (l1 and l2):
        if (l1.val < l2.val):
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next

    head.next = l1 if l1 != None else l2
    return prehead.next