class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #juntar arrays
        for i in range (n):
            nums1[m + i] = nums2[i]

        #ordenar array
        for i in range (m+n):
            for j in range ((m+n) - i - 1):
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
        return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution = Solution()
array = solution.merge(nums1, m, nums2, n)
print(array)
                    