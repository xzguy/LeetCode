class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.get_isomorphic_num(s) == self.get_isomorphic_num(t)

    def get_isomorphic_num(self, s: str) -> [int]:
        rank = 0
        iso_dict = {}
        num = []
        for c in s:
            if c not in iso_dict:
                rank += 1
                iso_dict[c] = rank
            num.append(iso_dict[c])
        return num

sol = Solution()
s = "egg"
t = "add"
print(sol.isIsomorphic(s, t))