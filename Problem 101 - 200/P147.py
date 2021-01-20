# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSort(self, nums: [int]):
        for i in range(1, len(nums)):
            j = i-1
            key = nums[i]
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums    

    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy_head = ListNode()
        cur = head
        while cur:
            prev_node = dummy_head
            next_node = prev_node.next
            while next_node:
                if cur.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next
            
            next_iter = cur.next
            cur.next = next_node
            prev_node.next = cur

            cur = next_iter
        return dummy_head.next
        
ll = ListNode(4)
ll.next = ListNode(2)
ll.next.next = ListNode(1)
ll.next.next.next = ListNode(3)
sol = Solution()
ll_sorted = sol.insertionSortList(ll)

print(sol.insertionSort([4, 2, 1, 3]))