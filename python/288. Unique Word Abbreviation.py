class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.hashmap = collections.defaultdict(set)
        for word in dictionary:
            abbr = self.helper(word)
            self.hashmap[abbr].add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.helper(word)
        words = self.hashmap[abbr]
        return len(words) == 0 or (len(words) == 1 and word in words)

    def helper(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
