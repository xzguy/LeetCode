def longestCommonPrefix(strs: [str]) -> str:
    if (not strs):
        return ''
    common_prefiex = ''
    end = False
    num = 0
    while (not end):
        c = ''
        for i in range(len(strs)):
            if num < len(strs[i]):
                if c == '':
                    c = strs[i][num]
                else:
                    if c != strs[i][num]:
                        end = True
            else:
                end = True
        num += 1
        if (not end):
            common_prefiex += c
    return common_prefiex

str_list = ["flower", "flow", "flight"]
print(longestCommonPrefix(str_list))