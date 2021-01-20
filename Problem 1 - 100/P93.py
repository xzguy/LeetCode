class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        if len(s) < 4 or len(s) > 12:
            return []
        res = []
        s_len = len(s)
        # each part should have length 1, 2 or 3
        for p1_len in range(1,4):
            if s_len - p1_len < 3 or int(s[:p1_len]) > 255 or \
                (s[0] == '0' and p1_len > 1):  # to avoid '01' and '00'
                continue
            for p2_len in range(1,4):
                p2_end = p1_len + p2_len
                if s_len - p2_end < 2 or int(s[p1_len : p2_end]) > 255 or \
                    (s[p1_len] == '0' and p2_len > 1):
                    continue
                for p3_len in range(1,4):
                    p3_end = p2_end + p3_len
                    if s_len <= p3_end or int(s[p2_end : p3_end]) > 255 or int(s[p3_end:]) > 255 or \
                        (s[p2_end] == '0' and p3_len > 1) or \
                        (s[p3_end] == '0' and s_len - p3_end > 1):
                        continue
                    res.append(s[:p1_len] + "." + s[p1_len:p2_end] + "." + \
                        s[p2_end:p3_end] + "." + s[p3_end:])
        return res

    # the logic in this method may be easier.
    def restoreIpAddresses_1(self, s: str) -> [str]:
        res = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a+b+c+d == len(s):
                            A = int(s[:a])
                            B = int(s[a:a+b])
                            C = int(s[a+b:a+b+c])
                            D = int(s[a+b+c:a+b+c+d])
                            if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                                ans = str(A) + "." + str(B) + "." + str(C) + "." + str(D)
                                if len(ans) == len(s)+3:
                                    res.append(ans)
        return res

    # solve it recursively
    def restoreIpAddresses_2(self, s: str) -> [str]:
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s: str, idx: int, path: str, res: list) -> None:
        if idx == 4:
            if not s:
                # delete last "." in the path
                res.append(path[:-1])
            return
        for i in range(1, len(s)+1):
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)
        
sol = Solution()
#print(sol.restoreIpAddresses('25525511135'))
print(sol.restoreIpAddresses_2('010010'))