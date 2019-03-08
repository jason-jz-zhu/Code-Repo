# dfs
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S or len(S) == 0:
            return ['']
        res = []
        self.dfs(list(S), 0, res)
        return res

    def dfs(self, S, index, res):
        if index == len(S):
            res.append(''.join(S))
            return

        self.dfs(S, index + 1, res)
        if S[index].isalpha():
            S[index] = chr(ord(S[index]) ^ 32)
            self.dfs(S, index + 1, res)
            S[index] = chr(ord(S[index]) ^ 32)


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
