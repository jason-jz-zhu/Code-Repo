class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                return mid
            elif A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid
        return start if A[start] > A[end] else end
