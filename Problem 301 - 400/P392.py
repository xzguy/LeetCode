from collections import defaultdict
from bisect import bisect_left

class Solution:
    def isSubsequence_simple(self, s: str, t: str) -> bool:
        if not s: return True
        s_idx = 0
        for c_t in t:
            if c_t == s[s_idx]:
                s_idx += 1
                if s_idx == len(s):
                    return True
        return False
    
    # binary search with preprocessing
    # assuming input strings are only lower case 26 letters
    def isSubsequence_bs(self, s: str, t: str) -> bool:
        if not s: return True

        # construct a table containing index of each character
        idx_dict = dict()
        for i in range(len(t)):
            if ord(t[i]) < 97 or ord(t[i]) >= 97 + 26:
                AssertionError('Assume all input strings are lower case 26 letters.')
            if t[i] not in idx_dict:
                idx_dict[t[i]] = []
            idx_dict[t[i]].append(i)
        
        # binary search function to find minimum greater of target
        # return -1 if not found, otherwise return that index
        def bs(arr: [int], trgt: int) -> int:
            if len(arr) == 1:
                if trgt < arr[0]:
                    return arr[0]
                else:
                    return -1
            mid = len(arr)//2 - 1
            if arr[mid] > trgt:
                return bs(arr[ : mid+1], trgt)
            else:
                return bs(arr[mid+1 : ], trgt)

        # traverse string s, find minimum greater index of previous character index
        cur_idx = -1
        for i in range(len(s)):
            if s[i] not in idx_dict:
                return False
            arr = idx_dict[s[i]]
            idx = bs(arr, cur_idx)
            if idx != -1:
                cur_idx = idx
            else:
                return False

        return True

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def createMap(s : str):
            # create a map. key is char. value is index of apperance in acending order. 
            posMap = defaultdict(list)
            for i, char in enumerate(s):
                posMap[char].append(i)
            return posMap

        posMap = createMap(t)
        # lowBound is the minimum index the current char has to be at.
        lowBound = 0
        for char in s:
            if char not in posMap: return False
            charIndexList = posMap[char]
            # try to find an index that is larger than or equal to lowBound
            i = bisect_left(charIndexList, lowBound)
            if i == len(charIndexList): return False
            lowBound = charIndexList[i] + 1
        return True

s = "abc"
t = "ahbgadc"

sol = Solution()
#print(sol.isSubsequence(s, t))

x = {}
x['a'] = 6
x['b'] = [9, 3]
x['b'].append(7)
print(x['c'])
y = 'c' in x
print(y)