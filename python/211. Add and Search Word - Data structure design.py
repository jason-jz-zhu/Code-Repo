class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.isWord = False

class WordDictionary(object):

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
        cur = self.root
        for w in word:
            child = cur.childs.get(w)
            if not child:
                child = TrieNode()
                cur.childs[w] = child
            cur = child
        cur.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(word, 0 ,self.root)

    def searchHelper(self, w, start, cur):
        if start == len(w):
            return cur.isWord

        if w[start] in cur.childs:
            return self.searchHelper(w, start + 1, cur.childs.get(w[start]))
        elif w[start] == '.':
            for c in cur.childs:
                if self.searchHelper(w, start + 1, cur.childs.get(c)):
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
