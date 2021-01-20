def findSubstring(s: str, words: [str]) -> [int]:
    num_words = len(words)
    if num_words == 0: return []
    word_len = len(words[0])
    index_list = []
    for i in range(len(s) - num_words * word_len + 1):
        temp_list = words.copy()
        found_substring = False
        if s[i : i+word_len] in words:
            # temp words list
            temp_list.remove(s[i : i+word_len])
            found_substring = True
            j = 0
            while(temp_list):
                next_substr = s[i+word_len*(j+1): i+word_len*(j+2)]
                if next_substr in temp_list:
                    temp_list.remove(next_substr)
                else:
                    found_substring = False
                    break
                j += 1
            if found_substring:
                index_list.append(i)
    return index_list

s_1 = "barfoothefoobarman"
words_1 = ["foo","bar"]
#print(findSubstring(s_1, words_1))

s_2 = "wordgoodgoodgoodbestword"
words_2 = ["word","good","best","word"]
#print(findSubstring(s_2, words_2))

s_3 = "wordgoodgoodgoodbestword"
words_3 = ["word","good","best","good"]
print(findSubstring(s_3, words_3))