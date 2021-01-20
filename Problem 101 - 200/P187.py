import collections

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:
        DNA_10 = collections.defaultdict(int)
        for i in range(len(s)-9):
            DNA_10[s[i:i+10]] += 1
        res = []
        for seq in DNA_10:
            if DNA_10[seq] > 1:
                res.append(seq)
        return res

sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))