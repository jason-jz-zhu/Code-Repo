class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            else:
                return [lo + 1, hi + 1]
        return []

# -------2025----
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers is None or len(numbers) == 0:
            return []

        start, end = 0, len(numbers) - 1
        while start < end:
            s = numbers[start] + numbers[end]
            if s == target:
                return [start + 1, end + 1]
            elif s < target:
                start += 1
            else:
                end -= 1
        return []
