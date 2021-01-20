class Solution:
    def camelMatch(self, queries: [str], pattern: str) -> [bool]:
        res = []
        for query in queries:
            res.append(self.word_match(query, pattern))
        return res

    def word_match(self, query: str, pattern: str) -> bool:
        i = j = 0
        while i < len(query):
            if j < len(pattern) and query[i] == pattern[j]:
                i += 1
                j += 1
            elif query[i].islower():
                i += 1
            else:
                return False
        return j == len(pattern)