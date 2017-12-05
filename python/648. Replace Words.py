class TrieNode(object):
    def __init__(self):
        self.childs = collections.defaultdict(str)
        self.is_word = False

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if dict is None or len(dict) == 0:
            return sentence
        if sentence is None or len(sentence) == 0:
            return ''

        root = TrieNode()
        res = []

        for word in dict:
            self.insert(root, word)

        for word in sentence.split():
            res.append(self.search(root, word))

        return ' '.join(res)

    def insert(self, root, word):
        node = root
        for w in word:
            child = node.childs[w]
            if not child:
                child = TrieNode()
                node.childs[w] = child
            node = child
        node.is_word = True

    def search(self, root, word):
        node = root
        tmp = ''
        for w in word:
            child = node.childs[w]
            if not child:
                break
            tmp += w
            node = child
            if node.is_word:
                return tmp
        return word



class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if dict is None or len(dict) == 0:
            return sentence
        if sentence is None or len(sentence) == 0:
            return ''
        dictset = set(dict)

        def replace(word):
            for i in xrange(1, len(word)):
                if word[: i] in dictset:
                    return word[: i]
            return word

        return ' '.join(map(replace, sentence.split()))

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict = set(dict)
        sentence_list = sentence.split(' ')

        for i in range(len(sentence_list)):
            for j in dict:
                if sentence_list[i].startswith(j):
                    sentence_list[i] = j

        return ' '.join(sentence_list)
