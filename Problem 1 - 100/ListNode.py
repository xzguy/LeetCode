# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def construct_linked_list(nums: [int]) -> ListNode:
    head = ListNode(0)
    pre = head
    for i in range(len(nums)):
        pre.next = ListNode(nums[i])
        pre = pre.next
    return head.next

def destruct_linked_list(head: ListNode):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums