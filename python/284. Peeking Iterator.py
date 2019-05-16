# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.cache = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cache

    def next(self):
        """
        :rtype: int
        """
        res = self.cache
        self.cache = self.iter.next() if self.iter.hasNext() else None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cache is not None

# work with all types
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.done = False
        if self.iter.hasNext():
            self.top = self.iter.next()
        else:
            self.done = True

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.top

    def next(self):
        """
        :rtype: int
        """
        tmp = self.top
        if self.iter.hasNext():
            self.top = self.iter.next()
        else:
            self.done = True
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.done
