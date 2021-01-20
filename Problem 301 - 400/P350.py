'''
arr1 = [1,2,3,3,3]
arr2 = [2,3,4,4]
res = [2,3]
'''
import collections

class Solution:
    def func(self, arr1: [int], arr2: [int]) -> [int]:
        cnt1 = collections.Counter(arr1)
        cnt2 = collections.Counter(arr2)
        res = []
        for n in cnt1:
            if n in cnt2:
                # do not use append, because it will be [[]]
                res += [n] * min(cnt1[n], cnt2[n])
        return res
