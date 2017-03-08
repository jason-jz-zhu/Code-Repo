class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        # Write your code here
        if A is None:
            return -1
        start, end = 0, len(A) - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if abs(A[start] - target) > abs(A[end] - target):
            return end
        else:
            return start 
