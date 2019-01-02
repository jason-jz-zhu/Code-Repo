class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        c = collections.Counter(ages)
        res = 0
        for a in c:
            for b in c:
                if a == b:
                    if self.check(a, a):
                        res += c[a] * (c[a] - 1)
                else:
                    if self.check(a, b):
                        res += c[a] * c[b]
        return res
    def check(self, a, b):
        return False if (b <= int(0.5 * a) + 7) or b > a or (b > 100 and a < 100) else True
