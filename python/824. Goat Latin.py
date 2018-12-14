class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S is None or len(S) == 0:
            return ''
        vowel = ['a', 'e', 'i', 'o', 'u']
        S_list = S.split(' ')
        for i, s in enumerate(S_list):
            tmp = ''
            if s[0].lower() in vowel:
                tmp = s + 'ma'
            else:
                tmp = s[1:] + s[0] + 'ma'
            tmp += 'a' * (1 + i)
            S_list[i] = tmp
        return ' '.join(S_list)


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S is None or len(S) == 0:
            return ''

        def convert(word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[0]
            return word + 'ma'
        return ' '.join(convert(word) + 'a' * i
                       for i, word in enumerate(S.split(), 1))
        
