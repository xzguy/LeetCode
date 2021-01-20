class Solution:
    def func(self, pattern: str, s: str) -> bool:
        words = list(s.split(" "))
        p2w = {}
        w2p = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in p2w:
                if p2w[pattern[i]] != words[i]:
                    return False
            else:
                p2w[pattern[i]] = words[i]
            if words[i] in w2p:
                if w2p[words[i]] != pattern[i]:
                    return False
            else:
                w2p[words[i]] = pattern[i]
        return True