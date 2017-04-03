class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.find_kth(nums1, nums2, l / 2 + 1)
        else:
            smaller = self.find_kth(nums1, nums2, l / 2)
            bigger = self.find_kth(nums1, nums2, l / 2 + 1)
            return (smaller + bigger) / 2.0

    def find_kth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        a = A[k / 2 - 1] if len(A) >= k / 2 else None
        b = B[k / 2 - 1] if len(B) >= k / 2 else None

        if b is None or (a is not None and a < b):
            return self.find_kth(A[k / 2:], B, k - k / 2)
        return self.find_kth(A, B[k / 2:], k - k / 2)
