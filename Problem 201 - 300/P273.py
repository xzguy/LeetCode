class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        unit = [" Thousand", " Million", " Billion", " Trillion"]

        # convert number < 1000 to English
        def sub(num: int) -> str:
            res = ""
            if num >= 100:
                res += convert_digits_to_English(num // 100)
                res += " Hundred"
                num %= 100
            if len(res) > 0 and num > 0:
                res += " "
            if num >= 20:
                res += convert_tens_to_English(num-num%10)
                if num % 10 != 0:
                    res += " " + convert_digits_to_English(num % 10)
            elif num > 10:
                res += convert_teens_to_English(num)
            elif num == 10:
                res += "Ten"
            elif num > 0:
                res += convert_digits_to_English(num)
            return res

        def convert_digits_to_English(num: int) -> str:
            if num == 1: return "One"
            if num == 2: return "Two"
            if num == 3: return "Three"
            if num == 4: return "Four"
            if num == 5: return "Five"
            if num == 6: return "Six"
            if num == 7: return "Seven"
            if num == 8: return "Eight"
            if num == 9: return "Nine"

        def convert_tens_to_English(num: int) -> str:
            if num == 20: return "Twenty"
            if num == 30: return "Thirty"
            if num == 40: return "Forty"
            if num == 50: return "Fifty"
            if num == 60: return "Sixty"
            if num == 70: return "Seventy"
            if num == 80: return "Eighty"
            if num == 90: return "Ninety"

        def convert_teens_to_English(num: int) -> str:
            if num == 11: return "Eleven"
            if num == 12: return "Twelve"
            if num == 13: return "Thirteen"
            if num == 14: return "Fourteen"
            if num == 15: return "Fifteen"
            if num == 16: return "Sixteen"
            if num == 17: return "Seventeen"
            if num == 18: return "Eighteen"
            if num == 19: return "Nineteen"
        
        res = sub(num % 1000)
        num //= 1000
        u = 0
        while num > 0:
            n = sub(num % 1000)
            if len(n) > 0:
                if len(res) > 0:
                    res = n + unit[u] + " " + res
                else:
                    res = n + unit[u]
            num //= 1000
            u += 1
        return res

num = 1234567
sol = Solution()
print(sol.numberToWords(num))