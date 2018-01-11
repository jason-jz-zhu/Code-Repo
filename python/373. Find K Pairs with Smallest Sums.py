class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or len(nums1) == 0:
            return []
        if not nums2 or len(nums2) == 0:
            return []
        res = []
        heap = []
        size1, size2 = len(nums1), len(nums2)
        for x1 in range(size1):
            heapq.heappush(heap, (nums1[x1] + nums2[0], x1, 0))
        while len(res) < min(k, size1 * size2):
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < size2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
