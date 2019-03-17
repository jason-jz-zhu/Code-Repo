class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or len(wordList) == 0:
            return 0
        wordList = set(wordList)
        q = collections.deque([(beginWord, 1)])
        while q:
            curr_word, curr_len = q.popleft()
            if curr_word == endWord:
                return curr_len
            for i in range(len(curr_word)):
                head = curr_word[:i]
                tail = curr_word[i + 1:]
                for w in 'abcdefghijklmnopqrstuvwxyz':
                    if w != curr_word[i]:
                        tmp_word = head + w + tail
                        if tmp_word in wordList:
                            q.append((tmp_word, curr_len + 1))
                            wordList.remove(tmp_word)
        return 0

# level order
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or len(wordList) == 0:
            return 0
        if endWord not in wordList:
            return 0
        wordList.remove(endWord)
        wordList = set(wordList)
        q = collections.deque([(beginWord, 1)])
        while q:
            size = len(q)
            for _ in range(size):
                curr_word, curr_len = q.popleft()
                for i in range(len(curr_word)):
                    head = curr_word[:i]
                    tail = curr_word[i + 1:]
                    for w in 'abcdefghijklmnopqrstuvwxyz':
                        if w == curr_word[i]:
                            continue
                        next_word = head + w + tail
                        if next_word == endWord:
                            return curr_len + 1
                        if next_word in wordList:
                            q.append((next_word, curr_len + 1))
                            wordList.remove(next_word)
        return 0
