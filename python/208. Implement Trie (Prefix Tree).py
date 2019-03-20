class TrieNode:
    def __init__(self):
        self.childs = {}
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            if w not in node.childs:
                node.childs[w] = TrieNode()
            node = node.childs[w]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            if w not in node.childs:
                return False
            node = node.childs[w]
        return True if node.isWord else False


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for w in prefix:
            if w not in node.childs:
                return False
            node = node.childs[w]
        return True



class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        def dfs(word, node, i):
            if i == len(word):
                return node.is_word
            if word[i] not in node.children:
                return False
            if dfs(word, node.children[word[i]], i + 1):
                return True
            return False

        node = self.root
        return dfs(word, node, 0)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        def dfs(prefix, node, i):
            if i == len(prefix):
                return True
            if prefix[i] not in node.children:
                return False
            if dfs(prefix, node.children[prefix[i]], i + 1):
                return True
            return False

        node = self.root
        return dfs(prefix, node, 0)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
