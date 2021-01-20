def letterCombinations(digits: str) -> [str]:
    phone_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    def cartesian_prod(s_1: [str], s_2: [str]) -> [str]:
        if not s_1: return s_2
        if not s_2: return s_1
        ans = []
        for i in s_1:
            for j in s_2:
                ans.append(i + j)
        return ans
    res = []
    for c in digits:
        res = cartesian_prod(res, phone_dict[c])
    return res

digits = '9'
print(letterCombinations(digits))