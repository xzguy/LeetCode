class Solution:
    '''
    a -> (e)
    e -> (a, i)
    i -> (a, e, o, u)
    o -> (i, u)
    u -> (a)
    '''
    def countVowelPermutation(self, n: int) -> int:
        vowel = [1] * 5

        for _ in range(n-1):
            new_vowel = [0]*5
            # 'a'
            new_vowel[1] += vowel[0]
            # 'e'
            new_vowel[0] += vowel[1]
            new_vowel[2] += vowel[1]
            # 'i'
            new_vowel[0] += vowel[2]
            new_vowel[1] += vowel[2]
            new_vowel[3] += vowel[2]
            new_vowel[4] += vowel[2]
            # 'o'
            new_vowel[2] += vowel[3]
            new_vowel[4] += vowel[3]
            # 'u'
            new_vowel[0] += vowel[4]
            vowel = new_vowel
        return sum(vowel) % (10 ** 9 + 7)

sol = Solution()
print(sol.countVowelPermutation(1))
