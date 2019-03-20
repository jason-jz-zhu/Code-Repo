# dfs
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.dfs(S, 0, '', res)
        return res

    def dfs(self, S, i, path, res):
        if len(path) == len(S):
            res.append(path)
            return
        # keep curr
        self.dfs(S, i + 1, path + S[i], res)
        if not S[i].isalpha():
            return
        # change to opposite
        self.dfs(S, i + 1, path + chr(ord(S[i]) ^ (1 << 5)), res)


# bfs
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        for curr in S:
            if curr.isalpha():
                res = [prev + child for prev in res for child in [curr.upper(), curr.lower()]]
            else:
                res = [prev + curr for prev in res]
        return res
