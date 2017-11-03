class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        if str is None:
            return None
        self.reverse(str, 0, len(str) - 1)
        i = 0
        for j in range(len(str) + 1):
            if j == len(str) or str[j] == ' ':
                self.reverse(str, i, j - 1)
                i = j + 1

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
