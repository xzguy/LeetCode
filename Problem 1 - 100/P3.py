# time complexity: O(n^2)
def lengthOfLongestSubstring_v1(s: str) -> int:
    max_len = 0
    # a loop of each char in the str
    loc_set = set()
    for i in range(len(s)):
        loc_set.clear()
        for j in range(i, len(s)):
            # duplicate char found
            if s[j] in loc_set:
                break
            # a new char
            else:
                loc_set.add(s[j])
        loc_max = len(loc_set)
        if loc_max > max_len:
            max_len = loc_max
    return max_len

# time complexity: O(2n)
def lengthOfLongestSubstring_v2(s: str) -> int:
    max_len = 0
    i = 0
    j = 0
    str_len = len(s)
    iter_set = set()
    # implicitly assume i <= j
    while(j < str_len):
        # a new char
        if s[j] not in iter_set:
            iter_set.add(s[j])
            max_len = max(max_len, len(iter_set))
            j += 1
        # duplicate char found
        else:
            iter_set.remove(s[i])
            i += 1
    return max_len

# time complexity: O(n)
def lengthOfLongestSubstring_v3(s: str) -> int:
    max_len = 0
    i = 0
    # dictionary contains the latest index of a char
    index_dict = {}
    for j in range(len(s)):
        # if duplicate char found
        if s[j] in index_dict:
            i = max(index_dict[s[j]], i)
        max_len = max(max_len, j - i + 1)
        index_dict[s[j]] = j + 1
    return max_len
    
s = "pypw"

print(lengthOfLongestSubstring_v1(s))
print(lengthOfLongestSubstring_v2(s))
print(lengthOfLongestSubstring_v3(s))