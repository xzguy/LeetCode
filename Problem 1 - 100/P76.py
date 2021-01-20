class Solution:
    def minWindow_1(self, s: str, t: str) -> str:
        t_set = set(t)
        # initialize dictionary
        cur_dict = {}
        for c in t_set:
            cur_dict[c] = -t.count(c)
        # window traverse with left and right pointer
        l, r = 0, 1
        best_l, best_r = 0, 0
        min_len = len(s)+1
        forms = 0
        while r <= len(s):
            if s[r-1] in t_set:
                cur_dict[s[r-1]] += 1
                if cur_dict[s[r-1]] == 0:
                    forms += 1
                while l < r and forms == len(t_set):
                    while s[l] not in t_set:
                        l += 1
                    if r-l < min_len:
                        best_l, best_r = l, r
                        min_len = r-l
                    cur_dict[s[l]] -= 1
                    if cur_dict[s[l]] == -1:
                        forms -= 1
                    l += 1
            r += 1

        if best_r > 0:
            return s[best_l:best_r]
        return ''

    # double traverse, in first round, store the index of characters in 't'
    # this method may be faster when 's' contains a lot of characters not in 't'
    def minWindow_2(self, s: str, t: str) -> str:
        t_set = set(t)
        cur_dict = {}
        for c in t_set:
            cur_dict[c] = -t.count(c)
        index_dict = {}
        index_list = []
        for i in range(len(s)):
            if s[i] in t_set:
                index_dict[i] = s[i]
                index_list.append(i)
        # window traverse with left and right pointer
        l, r = 0, 1
        best_l, best_r = 0, 0
        min_len = len(s)+1
        forms = 0
        while r <= len(index_list):
            r_char = s[index_list[r-1]]
            cur_dict[r_char] += 1
            if cur_dict[r_char] == 0:
                forms += 1
            while l < r and forms == len(t_set):
                if index_list[r-1] - index_list[l] + 1 < min_len:
                    best_l, best_r = index_list[l], index_list[r-1] + 1
                    min_len = index_list[r-1] - index_list[l] + 1
                l_char = s[index_list[l]]
                cur_dict[l_char] -= 1
                if cur_dict[l_char] == -1:
                    forms -= 1
                l += 1
            r += 1

        if best_r > 0:
            return s[best_l:best_r]
        return ''


sol = Solution()

S = "ADOBECODEBANC"
T = "ABC"
print(sol.minWindow_1(S, T))