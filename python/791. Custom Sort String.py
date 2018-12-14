class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        hashmap = collections.Counter(T)
        res = []
        for c in S:
            res.append(c * hashmap[c])
            hashmap[c] = 0
        for c in hashmap:
            res.append(c * hashmap[c])
        return ''.join(res)
