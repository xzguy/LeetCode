class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists: [ListNode]) -> ListNode:
    def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
        prehead = head = ListNode(-1)

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 != None else l2
        return prehead.next

    if len(lists) == 0: return None
    interval = 1
    while (interval < len(lists)):
        for i in range(0, len(lists)-interval, interval*2):
            lists[i] = merge2Lists(lists[i], lists[i+interval])
        interval *= 2

    return lists[0]