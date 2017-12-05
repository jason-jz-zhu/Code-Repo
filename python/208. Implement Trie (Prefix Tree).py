class TrieNode(object):
    def __init__(self):
        self.childs = collections.defaultdict(str)
        self.is_word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self._root
        for w in word:
            child = node.childs[w]
            if not child:
                child = TrieNode()
                node.childs[w] = child
            node = child
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self._root
        for w in word:
            child = node.childs[w]
            if not child:
                return False
            node = child
        return True if node.is_word else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self._root
        for w in prefix:
            child = node.childs[w]
            if not child:
                return False
            node = child
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
