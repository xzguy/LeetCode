class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or k == 0:
        return head

    new_end = head
    old_end = head
    L = 1
    while old_end.next:
        old_end = old_end.next
        L += 1
        if L > k+1:
            new_end = new_end.next

    if k % L == 0:
        return head

    rotate_len = 0    
    if L < k:
        rotate_len = L - (k%L)-1
    while rotate_len > 0:
        new_end = new_end.next
        rotate_len -= 1

    # rotate
    new_head = new_end.next
    new_end.next = None
    old_end.next = head
    return new_head