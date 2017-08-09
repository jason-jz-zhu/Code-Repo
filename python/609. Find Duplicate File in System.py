class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        hashmap = collections.defaultdict(list)
        for path in paths:
            s = path.split(' ')
            for i in xrange(1, len(s)):
                start, end = s[i].find('('), s[i].find(')')
                file_name = s[0] + '/' + s[i][: start]
                file_content = s[i][start + 1: end]
                hashmap[file_content].append(file_name)
        res = []
        for key, val in hashmap.iteritems():
            if len(val) > 1:
                res.append(val)
        return res
