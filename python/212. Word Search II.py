class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board) == 0 or len(board[0]) == 0:
            return []
        m, n = len(board), len(board[0])
        res = []

        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, '', node, res)
        return res

    def dfs(self, board, i, j, path, node, res):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        if node.is_word:
            res.append(path)
            node.is_word = False
            return
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] not in node.children:
            return

        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            board[i][j], tmp = '#', board[i][j]
            self.dfs(board, x, y, path + tmp, node.children[tmp], res)
            board[i][j] = tmp
                # return True
            # board[i][j] = tmp
        # return False
