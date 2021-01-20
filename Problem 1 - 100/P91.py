'''
The strategy is like the recursive sequence.
The number of decoding "D1,D2, ..., Dn" comes from two sourses:
it can be interpreted as
    "D1,D2, ..., Dn-1" and "Dn"; if "Dn" is not "0"
or
    "D1,D2, ..., Dn-2" and "Dn-1,Dn"; if "Dn-1,Dn" is valid (10 <= "Dn-1,Dn" <= 26)
We need a dummy start for number of decoding empty input is 1.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        for i in range(1, len(s)):
            if s[i] == "0" and s[i-1] != "1" and s[i-1] != "2":
                return 0

        # res[i] is the number of decodings for s[:i]
        res = [0] * (len(s) + 1)
        res[0] = 1
        res[1] = 1
        for i in range(1, len(s)):
            # the first source from above analysis
            if s[i] != "0":
                res[i+1] = res[i]
            # the second source from above analysis
            if int(s[i-1:i+1]) >= 10 and int(s[i-1:i+1]) <= 26:
                res[i+1] += res[i-1]
        return res[-1]
        
    # this method does not use dummy start
    def numDecodings_1(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1] != '1' and s[i-1] != '2':
                return 0

        nums = [0] * len(s)
        nums[0] = 1
        for i in range(1, len(s)):
            if s[i] == '0':
                # nums[i-1] > nums[i-2] means s[i-1] has been used
                # for constructing 11 <= .. <= 26, but since s[i] is
                # zero, so that construction is invalid.
                if i >= 2 and nums[i-1] > nums[i-2]:
                    nums[i] = nums[i-2]
                else:
                    nums[i] = nums[i-1]
            else:
                if int(s[i-1:i+1]) >= 11 and int(s[i-1:i+1]) <= 26:
                    if i == 1:
                        nums[i] = 2
                    else:
                        nums[i] = nums[i-1] + nums[i-2]
                else:
                    nums[i] = nums[i-1]
        return nums[-1]
        
sol = Solution()
print(sol.numDecodings('10210'), '= 1')
print(sol.numDecodings('1212'), '= 5')
print(sol.numDecodings('12312'), '= 6')
print(sol.numDecodings('94521'), '= 2')
print(sol.numDecodings('54236'), '= 2')
print(sol.numDecodings('121212'), '= 13')
print(sol.numDecodings('12121'), '= 8')