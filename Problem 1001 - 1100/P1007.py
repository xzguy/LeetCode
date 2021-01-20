class Solution:
    '''
    If the rotation exists, first find the number that
    only appears in A or B after some rotations.
    '''
    def minDominoRotations(self, A: [int], B: [int]) -> int:
        if len(A) == 1:
            if A[0] == B[0]:
                return 0
            else:
                return -1
        candidates = set()
        candidates.add(A[0])
        candidates.add(B[0])
        for i in range(1, len(A)):
            if A[i] not in candidates and B[i] not in candidates:
                return -1
            elif A[i] in candidates and B[i] in candidates:
                if A[i] == B[i]:
                    candidates = {A[i]}
            elif A[i] in candidates:
                candidates = {A[i]}
            else:
                candidates = {B[i]}
        candidate = candidates.pop()
        cnt_A = A.count(candidate)
        cnt_B = B.count(candidate)
        return len(A) - max(cnt_A, cnt_B)
        #return min([cnt_A, len(A)-cnt_A, cnt_B, len(B)-cnt_B])

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
sol = Solution()
print(sol.minDominoRotations(A, B))