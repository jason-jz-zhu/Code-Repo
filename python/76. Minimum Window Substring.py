class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ''
        tCounter = collections.Counter(t)
        cnt = 0
        sCounter = collections.defaultdict(int)
        left = right = 0
        minLen = float('inf')
        while right < len(s):

            if s[right] in tCounter and sCounter[s[right]] < tCounter[s[right]]:
                cnt += 1
            sCounter[s[right]] += 1
            while left <= right and cnt == len(t):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    res = s[left: right + 1]
                sCounter[s[left]] -= 1
                if s[left] in tCounter and sCounter[s[left]] < tCounter[s[left]]:
                    cnt -= 1

                left += 1
            right += 1
        return res
