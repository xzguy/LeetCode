# Definition for singly-linked list.
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
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

    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy
        carry = 0
        while l1 or l2 or carry:
            head.next = ListNode()
            head = head.next
            if l1 and l2:
                new_val = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                if carry:
                    new_val = (l1.val + carry) % 10
                    carry = (l1.val + carry) // 10
                else:
                    new_val = l1.val
                l1 = l1.next
            elif l2:
                if carry:
                    new_val = (l2.val + carry) % 10
                    carry = (l2.val + carry) // 10
                else:
                    new_val = l2.val
                l2 = l2.next
            else:
                new_val = carry
                carry = 0
            head.val = new_val
        return dummy.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
ll = sol.addTwoNumbers(l1, l2)
print(ll)