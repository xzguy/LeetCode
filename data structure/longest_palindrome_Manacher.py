def longest_palindrome(s: str):
    '''
    since Manacher's algorithm works for odd palindrome,
    we insert a bogus character to make the original string
    into an odd palindrome.
    '''

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
    longest_palindrome_in_odd_s = 2 * max_radius + 1
    longest_palindrome_in_s = (longest_palindrome_in_odd_s - 1) // 2

    center_idx = palindrome_radius.index(max_radius)
    longest_palindrome_str = odd_s[center_idx-max_radius : center_idx+max_radius+1]
    longest_palindrome_str = longest_palindrome_str[1:-1:2]
    
    return longest_palindrome_in_s, longest_palindrome_str

s = 'abacaacabab'
# s = 'babac'
# s = "babad"
# s = "cbbd"
# s = "a"
# s = "ac"
print(longest_palindrome(s))