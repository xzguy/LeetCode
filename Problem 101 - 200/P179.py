from functools import cmp_to_key

class LargerNumKey(str):
    # default less than function for sort (reverse order)
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    '''
    The key point in this problem is to compare
    a string A with string B, which number is bigger:A+B or B+A?
    We can sort these strings with condition:
        if A+B > B+A, then A > B, otherwise vice versa
    These comparing operation is transitive.
    string compare is enough here, for example, "993" > "992" is true

    The 'sort' is in reverse order. for example '9' > '92', '9' should be
    on the left side of '92'
    '''
    def largestNumber(self, nums: [int]) -> str:
        nums_str = map(str, nums)
        largest_num = ''.join(sorted(nums_str, key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

    def largestNumber_1(self, nums: [int]) -> str:
        if not any(nums):
            return '0'
        return ''.join(sorted(map(str, nums), key = cmp_to_key(lambda x, y: -1 if x+y > y+x else (1 if x+y < y+x else 0))))

nums = [3,30,34,5,9]
sol = Solution()
print(sol.largestNumber(nums))