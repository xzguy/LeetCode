class Solution:
    # dynamic programming way
    def isInterleave_1(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        mat = [[0] * (len(s1)+1) for i in range(len(s2)+1)]
        # initialize first row
        i = 0
        while i < len(s1) and s3[i] == s1[i]:
            mat[0][i+1] = 1
            i += 1
        # initialize first column
        i = 0
        while i < len(s2) and s3[i] == s2[i]:
            mat[i+1][0] = 1
            i += 1
        # build the path-matrix
        for c in range(1, len(s1)+1):
            for r in range(1, len(s2)+1):
                if mat[r][c-1] == 1 and s1[c-1] == s3[c+r-1]:
                    mat[r][c] = 1
                if mat[r-1][c] == 1 and s2[r-1] == s3[c+r-1]:
                    mat[r][c] = 1
        return mat[-1][-1] == 1

    # in-order tree traverse by recursion
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        c = s3[0]
        if c == s1[0] and c == s2[0]:
            return self.isInterleave(s1[1:], s2, s3[1:]) or \
                self.isInterleave(s1, s2[1:], s3[1:])
        if c == s1[0]:
            return self.isInterleave(s1[1:], s2, s3[1:])
        if c == s2[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        return False
            
s1 = "bbca"
s2 = "bcc"
s3 = "bbcbcac"
sol = Solution()
print(sol.isInterleave(s1, s2, s3))
print(sol.isInterleave_1(s1, s2, s3))