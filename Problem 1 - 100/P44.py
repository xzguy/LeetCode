'''
Analysis:
    The key point in this problem is '*'. For some string and
pattern, there may be multiple ways for matching. When there
is a '*', we iterate all possibilities of star covering by
indicate the last star match.
'''
def isMatch_iterate(s: str, p: str) -> bool:
    s_ptr = 0
    p_ptr = 0
    star_index = -1
    one_after_star_match_end = 0
    p_len = len(p)

    while (s_ptr < len(s)):
        if (p_ptr < p_len and p[p_ptr] in {s[s_ptr], '?'}):
            p_ptr += 1
            s_ptr += 1
        # always store pointer of last '*'
        elif (p_ptr < p_len and p[p_ptr] == '*'):
            star_index = p_ptr
            one_after_star_match_end = s_ptr
            p_ptr += 1
        # either not matching and no '*' or p_ptr == p_len
        elif (star_index != -1):
            p_ptr = star_index + 1
            one_after_star_match_end += 1
            s_ptr = one_after_star_match_end
        else:
            return False
        
    # if input string is empty
    while (p_ptr < p_len and p[p_ptr] == '*'):
        p_ptr += 1

    return p_ptr == p_len


s = "adceb"
p = "*a*b"
print(isMatch_iterate(s, p))
