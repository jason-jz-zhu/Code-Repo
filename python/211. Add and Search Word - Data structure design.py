class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for w in word:
            if w not in curr.childs:
                curr.childs[w] = TrieNode()
            curr = curr.childs[w]
        curr.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(w, curr, i):
            if i == len(w):
                return curr.isWord
            if w[i] == '.':
                for child in curr.childs.values():
                    if dfs(w, child, i + 1):
                        return True
            elif w[i] in curr.childs:
                if dfs(w, curr.childs[w[i]], i + 1):
                    return True
            return False

        curr = self.root
        return dfs(word, curr, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
