# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0:
            return 0

        res = 0
        for l in nestedList:
            res += self.dfs(l, 1)

        return res

    def dfs(self, nestedList, depth):

        s = 0
        if nestedList.isInteger():
            s += nestedList.getInteger() * depth
        else:
            for l in nestedList.getList():
                s += self.dfs(l, depth + 1)

        return s


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0:
            return 0

        return self.dfs(nestedList, 1)

    def dfs(self, nestedList, depth):
        if len(nestedList) == 0:
            return 0

        s = 0
        for l in nestedList:
            if l.isInteger():
                s += l.getInteger() * depth
            else:
                s += self.dfs(l.getList(), depth + 1)

        return s

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0:
            return 0

        stack = []
        s = 0
        for l in nestedList:
            stack.append((l, 1))

        while stack:
            curr, depth =  stack.pop()
            if curr.isInteger():
                s += curr.getInteger() * depth
            else:
                for i in curr.getList():
                    stack.append((i, depth + 1))

        return s
