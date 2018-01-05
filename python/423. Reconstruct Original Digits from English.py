class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        counter = collections.Counter(s)
        res = ''
        cache = [0] * 10
        cache[0] = counter['z']
        cache[2] = counter['w']
        cache[4] = counter['u']
        cache[6] = counter['x']
        cache[8] = counter['g']
        cache[1] = counter['o'] - cache[0] - cache[2] - cache[4]
        cache[3] = counter['h'] - cache[8]
        cache[5] = counter['f'] - cache[4]
        cache[7] = counter['s'] - cache[6]
        cache[9] = counter['i'] - cache[5] - cache[6] - cache[8]
        for i in range(len(cache)):
            res += str(i) * cache[i]
        return res
