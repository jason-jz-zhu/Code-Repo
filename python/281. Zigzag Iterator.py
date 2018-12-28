class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.i = 0
        self.size = max(len(v1), len(v2))
        self.tmp = []
        for i in range(self.size):
            if i < len(v1):
                self.tmp.append(v1[i])
            if i < len(v2):
                self.tmp.append(v2[i])


    def next(self):
        """
        :rtype: int
        """
        res = self.tmp[self.i]
        self.i += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.tmp)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
