class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if strings is None or len(strings) == 0:
            return []

        hashmap = collections.defaultdict(list)

        for s in strings:
            key = self.hashStr(s)
            hashmap[key].append(s)

        return hashmap.values()

    def hashStr(self, s):
        res = ''
        for i in range(1, len(s)):
            res += unichr((ord(s[i]) - ord(s[i - 1]) + 26) % 26)
        return res
        
