class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        if time is None or len(time) == 0:
            return ''
        h, m = time.split(':')
        hashset = set([y for x in (h, m) for y in x])
        curr = int(h) * 60 + int(m)
        res = ''

        for i in range(curr + 1, curr + 1441):
            t = i % 1440
            h, m = t / 60, t % 60
            res = '{:02d}:{:02d}'.format(h, m)
            if all([x in hashset for x in res if x != ':']):
                return res

        return ''
        
