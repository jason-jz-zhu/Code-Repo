class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import collections
        if s is None or len(s) == 0:
            return []
        counter = collections.Counter(s)
        mid = ''.join(k for k, v in counter.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k, v in counter.iteritems())
        return self.helper(mid, chars) if len(mid) < 2 else []

    def helper(self, mid, chars):
        res = []
        visited = [False] * len(chars)
        self.dfs(chars, visited, mid, [], res)
        return res

    def dfs(self, chars, visited, mid, path, res):
        if len(path) == len(chars):
            half = ''.join(path)
            res.append(half + mid + half[::-1])
            return
        for i in range(len(chars)):
            if visited[i] or (i != 0 and chars[i] == chars[i - 1] and not visited[i - 1]):
                continue
            visited[i] = True
            self.dfs(chars, visited, mid, path + [chars[i]], res)
            visited[i] = False
