# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    convert linked list to list first, then map to tree
    '''
    def sortedListToBST_1(self, head: ListNode) -> TreeNode:
        tree_list = []
        while head:
            tree_list.append(head.val)
            head = head.next
        
        def buildBST(start: int, end: int) -> TreeNode:
            if start == end:
                return None
            mid = (start + end) // 2
            root = TreeNode(tree_list[mid])
            root.left = buildBST(start, mid)
            root.right = buildBST(mid+1, end)
            return root

        return buildBST(0, len(tree_list))

    '''
    use fast and slow pointer to get middle of linked list,
    then map to tree recursively
    '''
    def sortedListToBST_2(self, head: ListNode) -> TreeNode:

        def sub(h: ListNode, tail: ListNode) -> TreeNode:
            if h == tail:
                return None
            slw, fst = h, h
            while fst != tail and fst.next != tail:
                slw = slw.next
                fst = fst.next.next
            root = TreeNode(slw.val)
            root.left = sub(h, slw)
            root.right = sub(slw.next, tail)
            return root
            
        return sub(head, None)

    '''
    since in-order traverse of BST coincide the linked list,
    simulate the tree traverse, and move linked list sequentially
    '''
    def sortedListToBST_3(self, head: ListNode) -> TreeNode:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        
        def sub(start: int, end: int) -> TreeNode:
            nonlocal head
            if start == end:
                return None
            mid = (start + end) // 2
            node = sub(start, mid)
            t = TreeNode(head.val)
            t.left = node

            head = head.next
            t.right = sub(mid+1, end)
            return t
            
        return sub(0, size)

ll = ListNode(-10)
ll.next = ListNode(-3)
ll.next.next = ListNode(0)
ll.next.next.next = ListNode(5)
ll.next.next.next.next = ListNode(9)

sol = Solution()
t = sol.sortedListToBST_3(ll)
print(t)