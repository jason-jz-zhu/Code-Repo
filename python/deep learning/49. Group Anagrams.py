class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs) == 0:
            return []

        map = {}
        res = []
        for word in strs:
            s_word = ''.join(sorted(word))
            if map.get(s_word) is None:
                map[s_word] = [word]
            else:
                map[s_word].append(word)

        for key, value in map.iteritems():
            res.append(value)

        return res
