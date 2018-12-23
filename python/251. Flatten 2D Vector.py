class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        tmp = [num for lst in vec2d if len(lst) > 0 for num in lst]
        self.stack = tmp[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack != []

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
