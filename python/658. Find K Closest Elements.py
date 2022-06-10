# remove begin or end element
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr is None or len(arr) == 0:
            return []
        res = arr
        while len(res) > k:
            left, right = 0, len(res) - 1
            if abs(x - res[0]) <= abs(x - res[-1]):
                res.pop()
            else:
                res.pop(0)
        return res

# binary search
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if arr is None or len(arr) == 0:
            return []
        if len(arr) == k:
            return arr
        start, end = 0, len(arr) - k
        while start + 1 < end:
            mid = start + (end - start) // 2
            if x - arr[mid] > arr[mid + k] - x:
                start = mid
            else:
                end = mid
        if abs(x - arr[start]) > abs(x - arr[start + k]):
            start = end
        return arr[start: start + k]

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = bisect.bisect_left(arr, x)
        left, right = i-1, i
        while k:
            if right >= len(arr) or \
                (left >= 0 and abs(arr[left]-x) <= abs(arr[right]-x)):
                left -= 1
            else:
                right += 1
            print left, right
            k -= 1
        return arr[left+1:right]
