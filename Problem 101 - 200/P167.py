class Solution:
    # use dictionary
    def twoSum(self, numbers: [int], target: int) -> [int]:
        complement_dict = {}
        for i in range(len(numbers)):
            if numbers[i] in complement_dict:
                return [complement_dict[numbers[i]]+1, i+1]
            complement_dict[target-numbers[i]] = i

    # use two pointers
    def twoSum_1(self, numbers: [int], target: int) -> [int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            if numbers[l] + numbers[r] < target:
                l +=1
            else:
                r -= 1

sol = Solution()
numbers = [2,7,11,15]
target = 9

numbers = [2,3,4]
target = 6

numbers = [-1,0]
target = -1

print(sol.twoSum_1(numbers, target))