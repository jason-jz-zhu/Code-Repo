class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []

        res = []
        self.helper(n, 0, 0, '', res)
        return res

    def helper(self, n, n_left, n_right, path, res):
        if n_left == n and n_right == n:
            res.append(path)
        if n_left < n:
            self.helper(n, n_left + 1, n_right, path + '(', res)
        if n_right < n_left:
            self.helper(n, n_left, n_right + 1, path + ')', res)
