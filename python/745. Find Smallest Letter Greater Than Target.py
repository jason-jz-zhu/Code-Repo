class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters is None or len(letters) == 0:
            return ''
        start, end = 0, len(letters) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if letters[mid] <= target:
                start = mid
            else:
                end = mid
        if target >= letters[end]:
            return letters[0]
        return letters[start] if letters[start] > target else letters[end]
