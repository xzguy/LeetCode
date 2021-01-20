import ListNode as ln

class Solution:
    def deleteDuplicates(self, head: ln.ListNode) -> ln.ListNode:
        dummy = ln.ListNode(0)
        dummy.next = head

        pre = dummy
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next

sol = Solution()
llist = ln.construct_linked_list([1,2,3,3,4,4,5])
print(ln.destruct_linked_list(llist))
print(ln.destruct_linked_list(sol.deleteDuplicates(llist)))