class Solution:
    # direct modeling
    def shortestPalindrome_1(self, s: str) -> str:
        i = 1
        while not self.is_palindrome(s):
            c = s[-i]
            s = s[:i-1] + c + s[i-1:]
            i += 1
        return s

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    # faster way, recursive way
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        for j in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == len(s):
            return s
        return ''.join(reversed(s[i:])) + self.shortestPalindrome(s[:i]) + s[i:]

    # KMP(Knuth–Morris–Pratt) lookup table
    def shortestPalindrome_2(self, s: str) -> str:
        pass