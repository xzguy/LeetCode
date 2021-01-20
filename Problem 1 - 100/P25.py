class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:
            r = r.next
            count += 1
        if count == k:  # reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, jump, l = pre, l, r
        else:
            return dummy.next