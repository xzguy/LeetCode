# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive merge sort
class Solution_1:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        start = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)

    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head

# bottom up merge sort (no recursive)
class Solution_2:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def getSize(head: ListNode) -> int:
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt

        def split(head: ListNode, size: int) -> ListNode:
            for _ in range(size-1):
                if not head:
                    break
                head = head.next

            if not head:
                return None
            next_start, head.next = head.next, None
            return next_start
        
        def merge(l1: ListNode, l2: ListNode, dummy_start: ListNode) -> ListNode:
            cur = dummy_start
            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next, l1 = l1, l1.next
                else:
                    cur.next, l2 = l2, l2.next
                cur = cur.next
            cur.next = l1 or l2
            # Find tail
            while cur.next:
                cur = cur.next
            # the returned tail should be the "dummy_start" node of next chunk
            return cur

        total_len = getSize(head)
        dummy = ListNode()
        dummy.next = head
        size = 1

        while size < total_len:
            dummy_start = dummy
            start = dummy.next
            while start:
                left = start
                right = split(left, size)
                start = split(right, size)
                dummy_start = merge(left, right, dummy_start)
            size *= 2
        return dummy.next