class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = collections.defaultdict(list)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.hashmap[len(word)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        tmp_list = self.hashmap[len(word)]
        if len(tmp_list) == 0:
            return False
        for tmp in tmp_list:
            cnt = 0
            for i in range(len(word)):
                if tmp[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
