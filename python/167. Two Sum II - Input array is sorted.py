class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, tail = 0, len(numbers) - 1
        while start < tail:
            if numbers[start] + numbers[tail] == target: 
                return [start + 1, tail + 1]
            if target < numbers[start] + numbers[tail]: tail = tail -1
            if target > numbers[start] + numbers[tail]: start = start + 1