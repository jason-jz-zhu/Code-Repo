class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        if s is None or len(s) == 0:
            return res
        partition = []
        self.dfs(s, 0, partition, res)
        return res

    def dfs(self, s, start_index, partition, res):
        if start_index == len(s):
            res.append(partition)
            return

        for i in xrange(start_index, len(s)):
            sub_string = s[start_index: i + 1]
            if not self.is_palindrome(sub_string):
                continue
            self.dfs(s, i + 1, partition + [sub_string], res)

    def is_palindrome(self, sub_string):
        i, j = 0, len(sub_string) - 1
        while i < j:
            if (sub_string[i] != sub_string[j]):
                return False
            i += 1
            j -= 1
        return True

            
