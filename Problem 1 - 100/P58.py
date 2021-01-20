def lengthOfLastWord(s: str) -> int:
    if not s: return 0

    word_start = -1
    if s[-1] != ' ':
        word_start = len(s) - 1
    for i in range(len(s)-2, -1, -1):
        if s[i] != ' ' and s[i+1] == ' ':
            word_start = i
        if s[i] == ' ' and s[i+1] != ' ':
            return word_start - i

    return word_start+1

input = " Helo    "
print(lengthOfLastWord(input))