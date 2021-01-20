# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    very tricky method from LeetCode.com
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_A, cur_B = headA, headB
        A_end_continue_at_B = False
        B_end_continue_at_A = False
        change_A_head = False
        change_B_head = False
        while cur_A and cur_B:
            if cur_A == cur_B:
                return cur_A
            if not cur_A.next and not A_end_continue_at_B:
                cur_A = headB
                A_end_continue_at_B = True
                change_A_head = True
            if not cur_B.next and not B_end_continue_at_A:
                cur_B = headA
                B_end_continue_at_A = True
                change_B_head = True
            if change_A_head:
                change_A_head = False
            else:
                cur_A = cur_A.next
            if change_B_head:
                change_B_head = False
            else:
                cur_B = cur_B.next
        return None

    # more concise code
    # the key point in this method is the guaranteed number of nodes
    # traversed after double traveresal. There will not loop infinitely.
    # If there is no intersection, after double traversal, both
    # cur_A and cur_B should be None, so they equal.
    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_A, cur_B = headA, headB
        while cur_A != cur_B:
            if cur_A:
                cur_A = cur_A.next
            else:
                cur_A = headB
            if cur_B:
                cur_B = cur_B.next
            else:
                cur_B = headA
        return cur_A
            
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = headA.next.next

sol = Solution()
print(sol.getIntersectionNode(headA, headB))