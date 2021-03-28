def expandPalindrome(s: str, left: int, right: int) -> int:
    L, R = left, right
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1


def longestPalindrome(s: str) -> str:
    if (s == None or len(s) < 1):
        return ""

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expandPalindrome(s, i, i)
        len2 = expandPalindrome(s, i, i+1)
        len_max = max(len1, len2)
        if len_max > end - start:
            start = i - (len_max-1) // 2
            end = i + len_max // 2
    return s[start: end+1]


s = "abadabca"
print(longestPalindrome(s))

class Solution:
    # time complexity O(len(s)^2), center-expand method
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for c in range(len(s)):
            
            # case 1, palindrome center is one character
            r = 1
            while c-r >=0 and c+r <len(s) and s[c-r] == s[c+r]:
                r += 1
            if 2*(r-1) + 1 > len(max_palindrome):
                max_palindrome = s[c-r+1:c+r]
            
            # case 2, palindrome center is two characters
            r = 1
            while c-r+1 >=0 and c+r <len(s) and s[c-r+1] == s[c+r]:
                r += 1
            if 2*(r-1) > len(max_palindrome):
                max_palindrome = s[c-r+2:c+r]
        return max_palindrome

    # time complexity O(len(s)), Manacher's method
    def longestPalindrome_Manacher(self, s: str) -> str:
        bogus_char = '#'
        odd_s = bogus_char + bogus_char.join([c for c in s]) + bogus_char
        palindrome_radius = [0] * len(odd_s)
        
        center = 0
        radius = 0

        while center < len(odd_s):
            # determine the longest palindrome starting at
            # center-radius and going  to center + radius
            while center - radius - 1 >= 0 and \
                    center + radius + 1 < len(odd_s) and \
                    odd_s[center-radius-1] == odd_s[center+radius+1]:
                radius += 1

            palindrome_radius[center] = radius

            old_center = center
            old_radius = radius
            center += 1
            radius = 0

            while center <= old_center + old_radius:
                mirror_center = 2*old_center - center
                max_mirror_radius = old_center + old_radius - center
                if palindrome_radius[mirror_center] < max_mirror_radius:
                    palindrome_radius[center] = palindrome_radius[mirror_center]
                    center += 1
                elif palindrome_radius[mirror_center] > max_mirror_radius:
                    palindrome_radius[center] = max_mirror_radius
                    center += 1
                else:
                    # palindrome_radius[mirror_center] == max_mirror_radius
                    radius = max_mirror_radius
                    break

        max_radius = max(palindrome_radius)
        center_idx = palindrome_radius.index(max_radius)
        longest_palindrome_str = odd_s[center_idx-max_radius : center_idx+max_radius+1]
        longest_palindrome_str = longest_palindrome_str[1:-1:2]
        
        return longest_palindrome_str

s = "cbbd"
s = "abadabca"
sol = Solution()
print(sol.longestPalindrome_Manacher(s))