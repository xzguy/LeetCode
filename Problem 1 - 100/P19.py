# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if head == None:
        return head

    l, r = head, head

    for i in range(n):
        r = r.next

    if r == None:
        return l.next

    while r.next != None:
        r = r.next
        l = l.next
    
    temp = l.next
    if temp == None:
        return None
    else:
        l.next = temp.next
    
    return head