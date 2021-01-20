class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        start = len(s)-1
        end = None
        start_word = False
        while start >= 0:
            if start_word:
                if s[start] == " ":
                    start_word = False
                    if not res:
                        res += s[start+1:end]
                    else:
                        res += " "+s[start+1:end]
                else:
                    pass
            else:
                if s[start] == " ":
                    pass
                else:
                    start_word = True
                    end = start+1
            start -= 1
        if start_word:
            if not res:
                res += s[:end]
            else:
                res += " "+s[:end]
        return res
    
    # use python built-in function split
    def reverseWords_1(self, s: str) -> str:
        after_split = s.split(" ")
        trimmed = [x for x in after_split if x]
        return " ".join(reversed(trimmed))


sol = Solution()
input = "the sky is blue"
input = "  hello world  "
input = "a good   example"
input = "apple"
input = "  Bob    Loves  Alice   "
print(sol.reverseWords_1(input))