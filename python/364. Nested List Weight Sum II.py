class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if nestedList is None or len(nestedList) == 0:
            return 0
        res = collections.defaultdict(int)
        self.dfs(nestedList, 0, res)
        if res is None or len(res) == 0:
            return 0
        s = 0
        max_depth = max(res.keys())
        for depth, sums in res.items():
            s += sums * (max_depth - depth + 1)
        return s

    def dfs(self, nestedList, depth, res):
        if len(nestedList) == 0:
            return

        for l in nestedList:
            if l.isInteger():
                res[depth] += l.getInteger()
            else:
                self.dfs(l.getList(), depth + 1, res)



class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList is None or len(nestedList) == 0:
            return 0

        res = []
        for l in nestedList:
            self.dfs(l, 0, res)

        s = 0
        for i in range(len(res) - 1, -1, -1):
            s += res[i] * (len(res) - i)

        return s


    def dfs(self, l, depth, res):
        if len(res) < depth + 1:
            res.append(0)
        if l.isInteger():
            res[depth] += l.getInteger()
        else:
            for ll in l.getList():
                self.dfs(ll, depth + 1, res)
