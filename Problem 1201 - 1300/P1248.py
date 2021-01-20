import collections

class Solution:
    '''
    Almost direct modeling, not very efficient.
    Use sliding window with double-end queue (deque).
    First, extend the window and push number into deque until having k odd numbers.
    After having k odds, popleft and count even numbers until popleft the first odd.
    Let's call number of evens on the left side 'left'.
    Then extend the window again, and count even numbers until reaching the k-th odd.
    Let's call number of evens on the right side 'right'.
    Then for that window of k odds, the total number of subarrays is 'left' * 'right'
    '''
    def numberOfSubarrays(self, nums: [int], k: int) -> int:
        res = 0
        num_odd = 0
        i = 0
        win = collections.deque()

        # get the first k odds
        while i < len(nums):
            win.append(nums[i])
            if nums[i] % 2 == 1:
                num_odd += 1
            i += 1
            if num_odd == k:
                break
        
        # if no such subarrays
        if num_odd < k:
            return 0

        left = 1
        right = 1
        # the rest part
        while i < len(nums):
            if num_odd == k:
                while win.popleft() % 2 == 0:
                    left += 1
                num_odd -= 1
            else:
                win.append(nums[i])
                if nums[i] % 2 == 0:
                    right += 1
                else:
                    num_odd += 1
                    res += left * right
                    left = 1
                    right = 1
                i += 1
        if num_odd == k:
            while win.popleft() % 2 == 0:
                left += 1
        res += left * right
        return res

    '''
    not using left*right, direct count
    '''
    def numberOfSubarrays_1(self, nums: [int], k: int) -> int:
        left = 0
        cnt = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                k -= 1
                cnt = 0
            while k == 0:
                if nums[left]  % 2 == 1:
                    k += 1
                left += 1
                cnt += 1
            res += cnt
        return res