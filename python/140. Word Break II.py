class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if s is None or len(s) == 0 or wordDict is None:
            return None
        can_break = [True for i in xrange(len(s) + 1)]
        Solution.res = []
        partition = []
        self.dfs(s, wordDict, partition, 0, can_break)
        return Solution.res

    def dfs(self, s, wordDict, partition, start_index, can_break):
        if start_index == len(s):
            Solution.res.append(' '.join(partition))
            return
        if not can_break[start_index]:
            return
        for i in xrange(start_index, len(s)):
            sub_string = s[start_index: i + 1]
            if sub_string not in wordDict:
                continue
            before_change = len(Solution.res)
            self.dfs(s, wordDict, partition + [sub_string], i + 1, can_break)
            if len(Solution.res) == before_change:
                can_break[i + 1] = False
