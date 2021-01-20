import math

class Solution:
    # Python built-in str(numerator/denominator) will use "e" instead of expending
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        GCD = math.gcd(numerator, denominator)
        numerator //= GCD
        denominator //= GCD

        sign = ""
        if numerator * denominator < 0:
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator >= denominator:
            integer_part = numerator // denominator
            numerator = numerator % denominator
        else:
            integer_part = 0
        if numerator == 0:
            return sign + str(integer_part)

        # if denominator only has factors of 2 or 5,
        # there is no recurring decimals, otherwise
        # the number has infinite recurring part.
        de = denominator
        while de % 2 == 0:
            de //= 2
        while de % 5 ==0:
            de //= 5
        # no infinite recurring
        # Python built-in str(numerator/denominator) will use "e" instead of expending
        if de == 1:
            return sign + str(integer_part + numerator/denominator)

        deci = ""
        idx = 0
        div_dict = {}
        while numerator not in div_dict:
            div_dict[numerator] = idx
            numerator *= 10
            deci += str(numerator//denominator)
            numerator %= denominator
            idx += 1
        rec_start = div_dict[numerator]
        return sign + str(integer_part) + "." + deci[:rec_start] + "(" + deci[rec_start:] + ")"

    # expanding all division instead of using "e"
    def fractionToDecimal_1(self, numerator: int, denominator: int) -> str:
        GCD = math.gcd(numerator, denominator)
        numerator //= GCD
        denominator //= GCD

        sign = ""
        if numerator * denominator < 0:
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)

        if numerator >= denominator:
            integer_part = numerator // denominator
            numerator = numerator % denominator
        else:
            integer_part = 0
        if numerator == 0:
            return sign + str(integer_part)

        deci = ""
        idx = 0
        div_dict = {}
        while numerator not in div_dict and numerator != 0:
            div_dict[numerator] = idx
            numerator *= 10
            deci += str(numerator//denominator)
            numerator %= denominator
            idx += 1
        if numerator == 0:
            res = sign + str(integer_part) + "." + deci
        else:
            rec_start = div_dict[numerator]
            res = sign + str(integer_part) + "." + deci[:rec_start] + "(" + deci[rec_start:] + ")"
        return res

sol = Solution()
numerator = -1
denominator = -6
print(sol.fractionToDecimal(numerator, denominator))