class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or len(strs) == 0:
            return []

        hashmap = collections.defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            hashmap[key].append(s)

        return hashmap.values()
