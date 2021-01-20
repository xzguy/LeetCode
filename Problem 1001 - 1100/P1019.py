# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> [int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        next_larger = [0]*len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    next_larger[i] = nums[j]
                    break
        return next_larger

    # one pass of linked list, with a stack to store
    # the number that has not found its next larger.
    # use amortized analysis (by average), time complexity
    # is O(n)
    def nextLargerNodes_1(self, head: ListNode) -> [int]:
        stack = []
        res = []
        while head:
            while stack and stack[-1][1] < head.val:
                pair = stack.pop()
                res[pair[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res