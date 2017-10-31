class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        if len(s) == 0:
            return True
        cnt_min = cnt_max = 0
        for i in s:
            cnt_max = cnt_max - 1 if i == ')' else cnt_max + 1
            cnt_min = cnt_min + 1 if i == '(' else max(cnt_min - 1, 0)
            if cnt_max < 0:
                return False
        return cnt_min == 0
