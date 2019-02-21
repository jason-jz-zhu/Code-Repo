class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        res = i = 0
        counter = collections.Counter()
        for j, x in enumerate(tree):
            counter[x] += 1
            while len(counter) >= 3:
                counter[tree[i]] -= 1
                if counter[tree[i]] == 0:
                    del counter[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
