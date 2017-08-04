class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1, l2 = len(version1), len(version2)
        i = j = 0
        while i < l1 or j < l2:
            v1 = v2 = 0
            while i < l1 and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < l2 and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
            j += 1
        return 0
