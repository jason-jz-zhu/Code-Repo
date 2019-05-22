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
