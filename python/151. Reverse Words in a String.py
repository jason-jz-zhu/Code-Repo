class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.strip().split()))
