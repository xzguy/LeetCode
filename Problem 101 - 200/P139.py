class Solution:
    # naive method
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        return False

    # use string pointers instead of string slicing
    def wordBreak_1(self, s: str, wordDict: [str]) -> bool:
        word_set = set(wordDict)

        def sub(start: int):
            if start == len(s) or s[start:] in word_set:
                return True
            for i in range(start, len(s)):
                if s[start:i+1] in word_set and sub(i+1):
                    return True
            return False

        return sub(0)
                
    # dynamic programming
    def wordBreak_2(self, s: str, wordDict: [str]) -> bool:
        f = [False for _ in range(len(s) + 1)]
        f[0] = True

        for i in range(1, len(s)+1):
            for word in wordDict:
                if len(word) <= i and f[i - len(word)] and s[i-len(word): i] == word:
                    f[i] = True
                    break
        return f[-1]

    # another dynamic programming
    def wordBreak_3(self, s: str, wordDict: [str]) -> bool:
        f = [False for _ in range(len(s) + 1)]
        f[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        return f[-1]



s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]

s = "goalspecial"
wordDict = ["go","goal","goals","special"]

s = "applepenapple"
wordDict = ["apple", "pen"]

sol = Solution()
print(sol.wordBreak_2(s, wordDict))