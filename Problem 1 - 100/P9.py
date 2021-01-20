import math

def isPalindrome(x: int) -> bool:
    if x < 0: return False
    if x == 0: return True

    num_digit = int(math.floor(math.log10(x)) + 1)

    half_len = num_digit // 2
    num = x
    while (half_len > 0):
        left_digit = num // 10**(num_digit-1)
        right_digit = num % 10
        if left_digit != right_digit:
            return False
        num -= left_digit * 10**(num_digit-1)
        num //= 10
        num_digit -= 2
        half_len = num_digit // 2
    return True

def isPalindrome_v2(x: int) -> bool:
	if x < 0: return False
	if x <= 9: return True
	num_digit = math.floor(math.log10(x)) + 1
	while num_digit > 1:
		high_digit = x // (10**(num_digit - 1))
		low_digit = x % 10
		if high_digit != low_digit: return False
		x -= high_digit * (10**(num_digit - 1))
		x //= 10
		num_digit -= 2
	return True


num = 1344431

print(isPalindrome(num))