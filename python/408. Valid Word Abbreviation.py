class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return False
        digits = [str(i) for i in xrange(10)]
        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            if abbr[j] not in digits[1:]:
                return False
            digits_start = j
            while j < len(abbr) and abbr[j] in digits:
                j += 1

            i += int(abbr[digits_start:j])
        return i == len(word) and j == len(abbr)

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))
