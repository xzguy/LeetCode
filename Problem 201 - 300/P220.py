class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, i+k+1):
                if j > len(nums)-1:
                    break
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    '''
    The key point here is to use bucket of size t+1.
    Each bucket can have at most only one number
    '''
    def containsNearbyAlmostDuplicate_1(self, nums: [int], k: int, t: int) -> bool:
        bucket = {}
        w = t+1
        for i in range(len(nums)):
            b = nums[i] // w
            if b in bucket:
                return True
            elif b+1 in bucket and abs(bucket[b+1] - nums[i]) <= t:
                return True
            elif b-1 in bucket and abs(bucket[b-1] - nums[i]) <= t:
                return True
            else:
                bucket[b] = nums[i]
            if i >= k:
                del bucket[nums[i-k]//w]
        return False
