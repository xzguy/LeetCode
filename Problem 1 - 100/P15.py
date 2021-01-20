import collections

def threeSum(nums: [int]) -> [[int]]:
    if len(nums) < 3: return []
    counter = collections.Counter(nums)
    tri = [[0,0,0]] if counter[0] > 2 else []
    negative = [x for x in counter if x < 0]
    positive = [x for x in counter if x >= 0]
    for n in negative:
        for p in positive:
            x = -n-p
            if x in counter:
                if x in {n, p} and counter[x] > 1:
                    tri.append([n, x, p])
                if x < n or x > p:
                    tri.append([n, x, p])
    return tri

nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))