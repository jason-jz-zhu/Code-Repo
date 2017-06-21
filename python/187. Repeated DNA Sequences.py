class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) < 10:
            return []
        map = collections.defaultdict(int)
        res = []
        for i in xrange(10, len(s) + 1):
            substr = s[i-10 : i]
            if substr in map:
                if map[substr] == 1:
                    res.append(substr)
                map[substr] += 1
            else:
                map[substr] = 1
        return res
