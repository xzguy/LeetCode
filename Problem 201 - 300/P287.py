'''
use a set, then find the duplicate
'''

class Solution:
    # not modify the original array
    def findDuplicate(self, nums: [int]) -> int:
        visited = set()
        for n in nums:
            if n in visited:
                return n
            visited.add(n)

    '''
    O(1) space complexity
    If we use a value as index, get the new number, it is like
    a permutation of N numbers, but since there are duplicate,
    there must exist smaller permutation. The duplicated number
    is the intersection of this process
    Think it as linked list, next item is access by the value as index.
    If we have two pointers, slow and fast, when they first meet
    at the intersection, fast has run exactly one circle than slow
    so, then slow starts from beginning again, the next meet is the duplicate.
    '''
    def findDuplicate_1(self, nums: [int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            # the first meet, fast-slow is exactly one circle
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
