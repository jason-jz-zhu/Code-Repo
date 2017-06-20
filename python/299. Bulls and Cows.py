class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if secret is None or len(secret) == 0:
            return None
        if guess is None or len(guess) == 0:
            return None
        if len(guess) != len(secret):
            return None
        bull, cow = 0, 0
        s_map, g_map = dict(), dict()
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                continue
            if g_map.get(secret[i], 0) > 0:
                cow += 1
                g_map[secret[i]] -= 1
            else:
                s_map[secret[i]] = s_map.get(secret[i], 0) + 1
            if s_map.get(guess[i], 0) > 0:
                cow += 1
                s_map[guess[i]] -= 1
            else:
                g_map[guess[i]] = g_map.get(guess[i], 0) + 1
        return str(bull) + 'A' + str(cow) + 'B'


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if secret is None or len(secret) == 0:
            return None
        if guess is None or len(guess) == 0:
            return None
        if len(guess) != len(secret):
            return None
        bulls = sum(map(operator.eq, secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
        return '%dA%dB' % (bulls, both - bulls)
