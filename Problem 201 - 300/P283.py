'''
two pass, while counting the number of zeros
and moving numbers forward on the fly
'''

class Solution:
    def move_zero(self, nums: [int]):
        N = len(nums)
        zeros = 0
        for i in range(N):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i-zeros] = nums[i]

        while zeros > 0:
            nums[N-zeros] = 0
            zeros -= 1