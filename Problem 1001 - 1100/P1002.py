import collections

class Solution:
    def commonChars(self, A: [str]) -> [str]:
        if not A:
            return []
        # first word
        cur_dict = self.get_char_count(A[0])
        # the rest words
        for i in range(1, len(A)):
            new_dict = self.get_char_count(A[i])
            for c in cur_dict:
                if c in new_dict:
                    cur_dict[c] = min(cur_dict[c], new_dict[c])
                else:
                    cur_dict[c] = 0
        res = []
        for c in cur_dict:
            for i in range(cur_dict[c]):
                res.append(c)
        return res

    def get_char_count(self, word: str):
        count = collections.defaultdict(int)
        for c in word:
            count[c] += 1
        return count

    # use counter, same logic
    def commonChars_1(self, A: [str]) -> [str]:
        if not A:
            return []
        # first word
        cur_dict = collections.Counter(c for c in A[0])
        # the rest words
        for i in range(1, len(A)):
            new_dict = collections.Counter(c for c in A[i])
            for c in cur_dict:
                if c in new_dict:
                    cur_dict[c] = min(cur_dict[c], new_dict[c])
                else:
                    cur_dict[c] = 0
        res = []
        for c in cur_dict:
            for i in range(cur_dict[c]):
                res.append(c)
        return res

sol = Solution()
A = ["bella","label","roller"]
A = ["cool","lock","cook"]
print(sol.commonChars_1(A))
                