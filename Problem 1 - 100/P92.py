# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_linked_list(nums: [int]) -> ListNode:
    head = ListNode(0)
    pre = head
    for i in range(len(nums)):
        pre.next = ListNode(nums[i])
        pre = pre.next
    return head.next

def destruct_linked_list(head: ListNode) -> [int]:
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        node_num = 1
        dummy = ListNode()
        dummy.next = head
        pre_m = None

        # reach the No.m node
        while node_num < m:
            if not head:
                print('error: link list length is less than m')
            pre_m = head
            head = head.next
            node_num += 1
        # reverse node between m and n
        pre = None
        while node_num <= n:
            if not head:
                print('error: link list length is less than n')
            head.next, pre, head = pre, head, head.next
            node_num += 1
        # link together
        if not pre_m:   # if not first part
            dummy.next.next = head
            return pre
        else:
            pre_m.next.next = head
            pre_m.next = pre

        return dummy.next

    # same method as the above, simpler code
    def reverseBetween_1(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode()
        dummy.next = head
        pre_m = dummy

        for _ in range(m-1):
            pre_m = pre_m.next

        # reverse [m, n] nodes
        pre = None
        cur = pre_m.next
        for _ in range(n-m+1):
            cur.next, pre, cur = pre, cur, cur.next

        pre_m.next.next = cur
        pre_m.next = pre

        return dummy.next
        
    # this method iteratively manages all links
    def reverseBetween_2(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre_m = dummy
        for _ in range(m-1):
            pre_m = pre_m.next
        
        cur = pre_m.next
        for _ in range(n-m):
            temp = pre_m.next
            pre_m.next = cur.next
            cur.next = cur.next.next
            pre_m.next.next = temp
        return dummy.next

    # general linked list reverse (iteratively)
    def reverse_iterative(self, head: ListNode) -> ListNode:
        cur = head
        pre = None

        while cur:
            cur.next, pre, cur = pre, cur, cur.next
            '''
            next_temp = cur.next
            cur.next = pre
            pre = cur
            cur = next_temp
            '''
        return pre

    # general linked list reverse (recursively)
    def reverse_recursive(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        last = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None
        return last

    '''
    The following method uses recursion
    '''
    # function to reverse first N elements of linked list
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        successor = None

        def sub(head: ListNode, n: int) -> ListNode:
            nonlocal successor
            if n == 1:
                successor = head.next
                return head
            last = sub(head.next, n-1)
            head.next.next = head
            head.next = successor
            return last
    
        return sub(head, n)

    def reverseBetween_recursion(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween_recursion(head.next, m-1, n-1)
        return head


llist = construct_linked_list([1,2])
print(destruct_linked_list(llist))
sol = Solution()
print(destruct_linked_list(sol.reverseBetween_recursion(llist, 1, 2)))

llist = construct_linked_list([1,2,3,4])
print(destruct_linked_list(sol.reverse_recursive(llist)))