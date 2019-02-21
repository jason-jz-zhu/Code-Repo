class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        size = len(nums1) + len(nums2)
        smaller = self.find_kth(nums1, 0, nums2, 0, (size + 1) // 2)
        bigger = self.find_kth(nums1, 0, nums2, 0, (size + 2) // 2)
        return (smaller + bigger) / 2

    def find_kth(self, nums1, i, nums2, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])
        v1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float('inf')
        v2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else float('inf')
        if v1 < v2:
            return self.find_kth(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self.find_kth(nums1, i, nums2, j + k // 2, k - k // 2)


class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        size = len(nums1) + len(nums2)
        smaller = self.find_kth(nums1, nums2, (size + 1) // 2)
        bigger = self.find_kth(nums1, nums2, (size + 2) // 2)
        return (smaller + bigger) / 2

    def find_kth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        v1 = nums1[k // 2 - 1] if k // 2 - 1 < len(nums1) else float('inf')
        v2 = nums2[k // 2 - 1] if k // 2 - 1 < len(nums2) else float('inf')
        if v1 < v2:
            return self.find_kth(nums1[k // 2: ], nums2, k - k // 2)
        else:
            return self.find_kth(nums1, nums2[k // 2: ], k - k // 2)
