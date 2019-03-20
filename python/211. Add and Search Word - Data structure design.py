class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(word, node, i):
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(word, child, i + 1):
                        return True
            elif word[i] in node.children:
                if dfs(word, node.children[word[i]], i + 1):
                    return True
            return False

        node = self.root
        return dfs(word, node, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
