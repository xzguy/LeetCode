import collections

class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        cnt = collections.defaultdict(int)
        for n in nums:
            cnt[n] += 1
        threshold = len(nums) // 3
        res = []
        for num in cnt:
            if cnt[num] > threshold:
                res.append(num)
        return res

    # another way, it first get the candidates
    # then test each candidates, it may not be faster
    def majorityElement_1(self, nums: [int]) -> [int]:
        # dummy initial values, it can be others
        candidates_1, candidates_2 = 0, 1
        cnt_1, cnt_2 = 0, 0
        for n in nums:
            if n == candidates_1:
                cnt_1 += 1
            elif n == candidates_2:
                cnt_2 += 1
            elif cnt_1 == 0:
                candidates_1 = n
                cnt_1 = 1
            elif cnt_2 == 0:
                candidates_2 = n
                cnt_2 = 1
            else:
                cnt_1 -= 1
                cnt_2 -= 1
        res = []
        if nums.count(candidates_1) > len(nums)//3:
            res.append(candidates_1)
        if nums.count(candidates_2) > len(nums)//3:
            res.append(candidates_2)
        return res