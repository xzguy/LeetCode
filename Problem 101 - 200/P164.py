import math

class Solution:
    # use Radix sort
    def maximumGap(self, nums: [int]) -> int:
        if len(nums) < 2:
            return None

        maxVal = max(nums)

        exp = 1
        radix = 10
        aux = [0 for _ in range(len(nums))]

        while (maxVal // exp > 0):
            count = [0 for _ in range(radix)]

            for i in range(len(nums)):
                count[(nums[i] // exp) % radix] += 1
        
            for i in range(1, len(count)):
                count[i] += count[i-1]

            for i in range(len(nums)-1, -1, -1):
                count[(nums[i] // exp) % radix] -= 1
                aux[count[(nums[i] // exp) % radix]] = nums[i]

            for i in range(len(nums)):
                nums[i] = aux[i]

            exp *= radix
        
        maxGap = 0
        for i in range(len(nums)-1):
            maxGap = max(maxGap, nums[i+1] - nums[i])
        return maxGap

    # try to avoid sort
    # use bucket and pigeonhole princile
    # put N numbers into evenly spaced N buckets
    # maximum gap only comes from gap between buckets
    def maximumGap_1(self, nums: [int]) -> int:
        if len(nums) < 2:
            return 0
        minValue = min(nums)
        maxValue = max(nums)
        if minValue == maxValue:
            return 0
        buckets = [[] for _ in range(len(nums))]
        bucket_size = (maxValue - minValue) / (len(nums)-1)
        # distribute numbers into buckets
        for n in nums:
            idx = math.floor((n-minValue) / bucket_size)
            buckets[idx].append(n)
        # loop through buckets for maximum gap
        pre_bucket_max = max(buckets[0])
        maxGap = float("-inf")
        for i in range(1, len(buckets)):
            if buckets[i]:
                maxGap = max(maxGap, min(buckets[i])-pre_bucket_max)
                pre_bucket_max = max(buckets[i])
        return maxGap

input = [3,65,92,1]
sol = Solution()
print(sol.maximumGap_1(input))