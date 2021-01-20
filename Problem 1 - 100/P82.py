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
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next

        return dummy.next

link_list = ln.construct_linked_list([1,1,1,1,2,2,2,3])


sol = Solution()
print(ln.destruct_linked_list(link_list))
print(ln.destruct_linked_list(sol.deleteDuplicates(link_list)))