# dfs
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []

        res = []
        hashmap = {0: '', 1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        self.dfs(digits, hashmap, 0, '', res)
        return res

    def dfs(self, digits, hashmap, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for i in hashmap[int(digits[index])]:
            self.dfs(digits, hashmap, index + 1, path + i, res)


# bfs
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []

        res = ['']
        hashmap = {0: '', 1: '', 2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

        for d in digits:
            tmp = []
            for prev in res:
                for curr in hashmap[int(d)]:
                    tmp.append(prev + curr)
            res = tmp
        return res
