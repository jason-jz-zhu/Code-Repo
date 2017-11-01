class StringIterator(object):
    import re
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.stack = []
        for pair in re.findall('\D\d+', compressedString):
            self.stack.append((pair[0], int(pair[1:])))
        self.stack = self.stack[::-1]


    def next(self):
        """
        :rtype: str
        """
        if len(self.stack) == 0:
            return ' '
        c, n = self.stack.pop()
        if n > 1:
            self.stack.append((c, n - 1))
        return c

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
