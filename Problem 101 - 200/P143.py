# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next

        visited = set()
        while head != slow:
            tail = self.get_tail(slow,visited)
            visited.add(tail)
            head.next, tail.next = tail, head.next
            head = tail.next
        slow.next = None

    def get_tail(self, head: ListNode, visited: set) -> ListNode:
        if not head:
            return None
        while head.next and head.next not in visited:
            head = head.next
        return head

    # in the above method, get_tail is duplicated.
    def reorderList_1(self, head: ListNode) -> None:
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next

        mid = slow
        tail_half = []
        while slow.next:
            tail_half.append(slow.next)
            slow = slow.next
        
        while tail_half:
            tail = tail_half.pop()
            head.next, tail.next = tail, head.next
            head = tail.next
        mid.next = None

    # reserve the half of the list
    def reorderList_2(self, head: ListNode) -> None:
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next

        # reverse the second half of linked list
        pre = None
        cur = slow.next
        if cur:
            post = cur.next
            while post:
                cur.next, pre, cur, post = pre, cur, post, post.next
            cur.next = pre
        slow.next = cur

        mid = slow
        slow = slow.next
        while slow:
            head.next, slow.next, head, slow = slow, head.next, head.next, slow.next
        mid.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol = Solution()
sol.reorderList_2(head)
print(head)