class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if words is None or len(words) == 0:
            return []
        row1 = 'qwertuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        res = []

        for word in words:
            cnt1 = cnt2 = cnt3 = 0
            for w in set(word):
                if w.lower() in row1:
                    cnt1 = 1
                if w.lower() in row2:
                    cnt2 = 1
                if w.lower() in row3:
                    cnt3 = 1
                if cnt1 + cnt2 + cnt3 > 1:
                    break
            if cnt1 + cnt2 + cnt3 == 1:
                res.append(word)
        return res
