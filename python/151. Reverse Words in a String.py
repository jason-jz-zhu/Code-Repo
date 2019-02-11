class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None

        res = s.strip()
        if len(res) == 0:
            return ''

        res = [c for c in res.split(' ') if c != '']
        return ' '.join(res[::-1])
