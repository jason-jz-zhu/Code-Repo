class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        import collections
        n1, n2 = len(s1), len(s2)
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2[:n1])
        if counter1 == counter2:
            return True
        for i in xrange(n1, n2):
            counter2[s2[i]] += 1
            counter2[s2[i - n1]] -= 1
            if counter2[s2[i - n1]] == 0:
                del counter2[s2[i - n1]]
            if counter1 == counter2:
                return True
        return False
