def twoSum_v1(nums, target):
    complement = set()
    for i in range(len(nums)):
        # found the pair
        if nums[i] in complement:
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j, i]
        # not found the pair
        else:
            complement.add(target - nums[i])
    return [-1, -1]

def twoSum(nums, target):
    complement_dict = {}
    for i in range(len(nums)):
        # found the pair
        if nums[i] in complement_dict:
            return [complement_dict[nums[i]], i]
        # not found the pair
        else:
            complement_dict[target - nums[i]] = i
    return [-1, -1]

num_list = [2, 7, 11, 15, 21, 89]
target = 9

print(twoSum(num_list, target))