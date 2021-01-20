def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    # assume nums1 has shorter or equal length, otherwise swap them
    m, n = len(nums1), len(nums2)
    if n < m:
        nums1, nums2, m, n = nums2, nums1, n, m
    if n == 0:
        raise ValueError

    imin, imax, mid_len = 0, m, (n + m + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = mid_len - i
        # i is too big
        if i > 0 and nums1[i-1] > nums2[j]:
            imax -= 1
        # i is too small
        # i < m implies j > 0
        elif i < m and nums2[j-1] > nums1[i]:
            imin += 1
        # perfect i
        else:
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])

            if (n + m) % 2 == 1:
                return max_of_left

            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            return (max_of_left + min_of_right) / 2.0

nums1 = [2]
nums2 = [1,3]
median = findMedianSortedArrays(nums1, nums2)

print(median)