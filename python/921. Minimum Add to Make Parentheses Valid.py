class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        bal = res = 0
        for s in S:
            bal += 1 if s == '(' else -1
            if bal == -1:
                bal += 1
                res += 1
        return res + bal
