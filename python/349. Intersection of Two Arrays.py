class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or len(nums1) == 0:
            return []
        if nums2 is None or len(nums2) == 0:
            return []

        nums1, nums2 = set(nums1), set(nums2)

        # return list(set(nums1) & set(nums2))

        return [num for num in nums1 if num in nums2]
