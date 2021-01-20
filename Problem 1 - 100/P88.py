class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return
        n1_idx = m-1
        n2_idx = n-1
        for i in range(m+n-1, -1, -1):
            if n1_idx >= 0 and n2_idx >= 0:
                if nums1[n1_idx] > nums2[n2_idx]:
                    nums1[i] = nums1[n1_idx]
                    n1_idx -= 1
                else:
                    nums1[i] = nums2[n2_idx]
                    n2_idx -= 1
            elif n2_idx >= 0:
                nums1[i] = nums2[n2_idx]
                n2_idx -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol = Solution()
print(sol.merge(nums1, m, nums2, n))