def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0: return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i] == needle[0]:
            complete = True
            for j in range(1, len(needle)):
                if haystack[i+j] != needle[j]:
                    complete = False
                    break
            if complete:
                return i
    return -1
