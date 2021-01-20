class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # compare two strings equal or not regardless of character order
        def str_equal_orderless(s1: str, s2: str) -> bool:
            if len(s1) != len(s2):
                return False
            l1 = sorted(list(s1))
            l2 = sorted(list(s2))
            for i in range(len(l1)):
                if l1[i] != l2[i]:
                    return False
            return True
        
        if s1 == s2:
            return True
        # compare two whole strings
        if not str_equal_orderless(s1, s2):
            return False
        # compare every partition's first parts
        for i in range(1, len(s1)):
            if str_equal_orderless(s1[:i], s2[:i]) and \
                self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            elif str_equal_orderless(s1[:i], s2[len(s1)-i:]) and \
                self.isScramble(s1[:i], s2[len(s1)-i:]) and self.isScramble(s1[i:], s2[:len(s1)-i]):
                return True
        return False
    

sol = Solution()
print(sol.isScramble("obobyrqd", "byorqdbo"), " = True")
print(sol.isScramble("hobobyrqd", "hbyorqdbo"), " = True")
print(sol.isScramble('dbdac', 'abcdd'), " = False")
print(sol.isScramble('abcdd', 'dbdac'), " = False")
print(sol.isScramble('a', 'a'), " = True")
print(sol.isScramble('ab', 'ba'), " = True")
print(sol.isScramble('great', 'rgeat'), " = True")
print(sol.isScramble('abcde', 'caebd'), " = False")