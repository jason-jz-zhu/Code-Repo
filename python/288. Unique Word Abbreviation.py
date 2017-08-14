class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self._lookup = collections.defaultdict(set)
        for word in dictionary:
            abbr = self.abbreviation(word)
            self._lookup[abbr].add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.abbreviation(word)
        words = self._lookup[abbr]
        return len(words) == 0 or (len(words) == 1 and word in words)

    def abbreviation(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word)-2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
