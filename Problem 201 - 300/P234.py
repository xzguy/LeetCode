# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        slow = fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        # odd number in linked list
        if fast:
            slow = slow.next
        # now slow points to the beginning of other half of isPalindrome
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True