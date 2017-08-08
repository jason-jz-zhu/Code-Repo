class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)
        for s in strings:
            hashmap[self.hashStr(s)].append(s)

        res = []
        for key, val in hashmap.iteritems():
            res.append(sorted(val))
        return res

    def hashStr(self, s):
        base = ord(s[0])
        hashcode = ''
        for i in xrange(len(s)):
            if ord(s[i]) - base >= 0:
                hashcode += unichr(ord('a') + ord(s[i]) - base)
            else:
                hashcode += unichr(ord('a') + ord(s[i]) - base + 26)
        return hashcode
