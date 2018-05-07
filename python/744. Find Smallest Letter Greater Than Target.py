class Solution:
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
            mid = int(start + (end - start) / 2)
            if letters[mid] <= target:
                start += 1
            else:
                end -=1
        if letters[start] > target:
            return letters[start]
        elif letters[end] > target:
            return letters[end]
        return letters[0]
