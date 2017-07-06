# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(n):
            if knows(res, i):
                res = i

        for i in xrange(n):
            if res != i and (knows(res, i) or not knows(i, res)):
                return -1

        return res

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashmap = [True for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(n):
                if hashmap[i] and i != j:
                    if knows(i, j) or not knows(j, i):
                        hashmap[i] = False
                    else:
                        hashmap[j] = False
            if hashmap[i]:
                return i

        return -1
