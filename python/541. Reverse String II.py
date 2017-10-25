class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''

        s_list = list(s)
        for i in range(0, len(s), 2 * k):
            if i + k > len(s_list):
                s_list[i:] = s_list[i:][::-1]
            else:
                s_list[i: i + k] = s_list[i: i + k][::-1]
        return ''.join(s_list)

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None or len(ransomNote) == 0:
            return True
        if magazine is None:
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
