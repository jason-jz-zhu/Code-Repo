class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        import collections
        if J is None or J == '':
            return 0
        if S is None or S == '':
            return 0
        hashmap = collections.defaultdict(int)
        res = 0
        for j in J:
            hashmap[j] += 1
        for s in S:
            if s in hashmap:
                res += 1
        return res
