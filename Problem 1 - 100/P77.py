class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

sol = Solution()
print(sol.combine(4, 2))