class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dictset = set(dict)

        def replace(word):
            for i in xrange(1, len(word)):
                if word[: i] in dictset:
                    return word[: i]
            return word

        return ' '.join(map(replace, sentence.split()))
