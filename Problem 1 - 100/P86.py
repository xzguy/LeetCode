import ListNode as ln

class Solution:
    def partition(self, head: ln.ListNode, x: int) -> ln.ListNode:
        dummy_lessThan_head = ln.ListNode(0)
        lessThan_cur = ln.ListNode(0)
        dummy_lessThan_head.next = lessThan_cur
        lessThan_pre = dummy_lessThan_head

        dummy_greaterEqual_head = ln.ListNode(0)
        greaterEqual_cur = ln.ListNode(0)
        dummy_greaterEqual_head.next = greaterEqual_cur
        greaterEqual_pre = dummy_greaterEqual_head

        while head:
            if head.val < x:
                lessThan_cur.val = head.val
                lessThan_cur.next = ln.ListNode(0)
                lessThan_pre = lessThan_cur
                lessThan_cur = lessThan_cur.next
            else:
                greaterEqual_cur.val = head.val
                greaterEqual_cur.next = ln.ListNode(0)
                greaterEqual_pre = greaterEqual_cur
                greaterEqual_cur = greaterEqual_cur.next
            head = head.next
        greaterEqual_pre.next = None
        lessThan_pre.next = dummy_greaterEqual_head.next
        return dummy_lessThan_head.next

sol = Solution()
llist = ln.construct_linked_list([1,4,3,2,5,2])
print(ln.destruct_linked_list(llist))
print(ln.destruct_linked_list(sol.partition(llist, 8)))