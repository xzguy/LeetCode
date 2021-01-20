class Solution:
    # naive method
    def minCut(self, s: str) -> int:
        
        def isPalindrome(s, start, end) -> bool:
            while end > start:
                if s[start] != s[end]:
                    return False
                end -= 1
                start += 1
            return True

        def helper(result: [int], temp_res: [str], start: int) -> None:
            if start == len(s):
                result.append(len(temp_res))
            else:
                for i in range(start, len(s)):
                    if isPalindrome(s, start, i):
                        temp_res.append(s[start : i+1])
                        helper(result, temp_res, i+1)
                        temp_res.pop()

        res = []
        helper(res, [], 0)
        return min(res)-1

    # fast method, greedy/dynamic programming way
    def minCut_1(self, s: str) -> int:
        # cut[i] stores the number of cuts for s[:i]
        # initialize cut[i] to i-1 (single letter palindrome)
        cut = [x-1 for x in range(len(s)+1)]

        # i is palindrome center
        # j is palindrome radius
        for i in range(len(s)):
            # odd palindrome length
            j = 0
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j]+1)
                j += 1
            # even palindrome length
            j = 1
            while i-j+1 >= 0 and i+j < len(s) and s[i-j+1] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j+1]+1)
                j += 1
        return cut[-1]


input = "cabababcbc"
sol = Solution()
print(sol.minCut_1(input))