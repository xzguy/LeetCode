def removeElement(nums: [int], val: int) -> int:
    n_len = len(nums)

    i = 0
    while (i < n_len):
        if nums[i] == val:
            del nums[i]
            n_len -= 1
        else:
            i += 1
    return n_len