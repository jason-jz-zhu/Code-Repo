from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)
        q = deque([(beginWord, 1)])
        wordLen = len(beginWord)
        while q:
            node, pathLen = q.popleft()
            if node == endWord: return pathLen
            for i in xrange(wordLen):
                head = node[:i]
                tail = node[i+1:]
                for w in 'abcdefghijklmnopqrstuvwxyz':
                    if node[i] != w:
                        tempWord = head + w + tail
                        if tempWord in wordSet:
                            q.append((tempWord, pathLen+1))
                            wordSet.remove(tempWord)
        return 0