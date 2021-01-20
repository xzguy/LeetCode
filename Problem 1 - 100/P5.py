def expandPalindrome(s: str, left: int, right: int) -> int:
    L, R = left, right
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1


def longestPalindrome(s: str) -> str:
    if (s == None or len(s) < 1):
        return ""

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandPalindrome(s, i, i)
        len2 = expandPalindrome(s, i, i+1)
        len_max = max(len1, len2)
        if len_max > end - start:
            start = i - (len_max-1) // 2
            end = i + len_max // 2
    return s[start: end+1]


s = "abadabca"
print(longestPalindrome(s))
