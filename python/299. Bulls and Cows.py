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

        s_hashmap = collections.Counter(secret)
        g_hashmap = collections.Counter(guess)

        bull = sum(i == j for i, j in zip(secret, guess))
        cow = sum((s_hashmap & g_hashmap).values()) - bull
        # cow = sum(min(secret.count(x), guess.count(x)) for x in '0123456789') - bull
        return '{}A{}B'.format(bull, cow)


        
