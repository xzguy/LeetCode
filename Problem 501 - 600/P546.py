class Solution:
    # direct modeling, not suggested
    def removeBoxes(self, boxes: [int]) -> int:
        
        def sub(A: [int], memo: dict) -> int:
            if len(A) == 1:
                return 1
            if tuple(A) not in memo:
                res = 0
                i = 0
                while i < len(A):
                    j = i
                    while j < len(A) and A[j] == A[i]:
                        j += 1
                    res = max(res, (j-i)**2 + sub(A[:i] + A[j:], memo))
                    i = j
                memo[tuple(A)] = res
            return memo[tuple(A)]

        return sub(boxes, {})

    # dp memo
    def removeBoxes_1(self, boxes: [int]) -> int:
        
        def dfs(left: int, right: int, runs: int, memo: dict) -> int:
            if left > right:
                return 0
            if (left, right, runs) not in memo:
                # since there are 'runs' boxes infront of boxes[left]
                # and they are the same color, if remove them all
                res = (runs+1)**2 + dfs(left+1, right, 0, memo)
                # if not moving these boxes, we may attach them to
                # infront of some other box with the same color
                for i in range(left+1, right+1):
                    if boxes[i] == boxes[left]:
                        res = max(res, dfs(left+1, i-1, 0, memo) + dfs(i, right, runs+1, memo))
                memo[left, right, runs] = res
            return memo[left, right, runs]

        return dfs(0, len(boxes)-1, 0, {})