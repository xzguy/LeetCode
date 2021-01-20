class Solution:
    # naive method
    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        res = []
        if s in wordDict:
            res.append(s)
        for i in range(1, len(s)):
            if s[:i] in wordDict:
                for string in self.wordBreak(s[i:], wordDict):
                    res.append(s[:i] + " " + string)
        return res

    # use string pointers instead of string slicing
    def wordBreak_1(self, s: str, wordDict: [str]) -> [str]:

        def sub(start: int) -> [str]:
            res = []
            if s[start:] in wordDict:
                res.append(s[start:])
            for i in range(start+1, len(s)):
                if s[start:i] in wordDict:
                    for string in sub(i):
                        res.append(s[start:i] + " " + string)
            print(start)
            return res
        
        return sub(0)

    # above method can have many duplicated calculation
    # use memo to store the intermediate results
    def wordBreak_2(self, s: str, wordDict: [str]) -> [str]:

        def sub(start: int, memo: dict) -> [str]:
            if start in memo:
                return memo[start]
            res = []
            if s[start:] in wordDict:
                res.append(s[start:])
            for i in range(start+1, len(s)):
                if s[start:i] in wordDict:
                    for string in sub(i, memo):
                        res.append(s[start:i] + " " + string)
            memo[start] = res
            print(start)
            return res
        
        return sub(0, {})

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]

s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]


sol = Solution()
print(sol.wordBreak_1(s, wordDict))