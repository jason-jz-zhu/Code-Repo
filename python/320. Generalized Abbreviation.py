class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if word is None or len(word) == 0:
            return ['']
        res = []
        self.helper(word, 0, 0, '', res)
        return res
    
    def helper(self, word, index, cnt, path, res):
        if len(word) == index:
            res.append(path + str(cnt) if cnt > 0 else path)
        else:
            self.helper(word, index + 1, cnt + 1, path, res)
            self.helper(word, index + 1, 0, path + (str(cnt) if cnt > 0 else '') + word[index], res)
