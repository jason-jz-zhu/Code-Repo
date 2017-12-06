class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) == 0:
            return []

        res = []
        hashmap = collections.defaultdict(int)

        for i in range(10, len(s) + 1):
            sub_str = s[i-10: i]
            if hashmap[sub_str] == 1:
                res.append(sub_str)
            hashmap[sub_str] += 1

        return res
