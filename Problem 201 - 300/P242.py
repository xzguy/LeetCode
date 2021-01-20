class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_set = set(t)
        s_set = set(s)
        if s_set != t_set:
            return False
        for i in t_set:
            if i not in s or s.count(i) != t.count(i):
                return False
        return True
        
s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))