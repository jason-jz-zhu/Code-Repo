class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for i in xrange(1, len(strs)):
            while strs[i][: len(prefix)] != prefix:
                prefix = prefix[: -1]
                if not prefix:
                    return ''
        return prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        for i in xrange(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
            
