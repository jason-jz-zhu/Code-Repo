class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateParenthesisRecu(res, '', 0, 0, n)
        return res

    def generateParenthesisRecu(self, res, current, left, right, n):
        if left == n and right == n:
            res.append(current)
        if left < n:
            self.generateParenthesisRecu(res, current + '(', left + 1, right, n)
        if right < left :
            self.generateParenthesisRecu(res, current + ')', left, right + 1, n)
