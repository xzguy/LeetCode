# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        curr = dummy_head
        sum_two = 0
        while(l1 != None or l2 != None):
            if l1 != None:
                sum_two += l1.val
                l1 = l1.next
            if l2 != None:
                sum_two += l2.val
                l2 = l2.next
            curr.next = ListNode(sum_two % 10)
            sum_two //= 10
            curr = curr.next
        if sum_two > 0:
            curr.next = ListNode(1)
            curr = curr.next
        return dummy_head.next