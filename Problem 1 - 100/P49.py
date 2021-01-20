def groupAnagrams(strs: [str]) -> [[str]]:
    strs.sort()
    anagram_dict = {}
    result = []
    for s in strs:
        if str(sorted(s)) in anagram_dict:
            anagram_dict[str(sorted(s))].append(s)
        else:
            anagram_dict[str(sorted(s))] = [s]
    for k in anagram_dict:
        result.append(anagram_dict[k])
    return result

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input))