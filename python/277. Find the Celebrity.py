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
        if n <= 0:
            return -1

        res = 0
        for i in range(n):
            if res != i and knows(res, i):
                res = i

        for i in range(n):
            if res != i and (knows(res, i) or not knows(i, res)):
                return -1

        return res

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return -1

        hashmap = [True] * n
        for i in range(n):
            for j in range(n):
                if hashmap[i] and i != j:
                    if knows(i, j) or not knows(j, i):
                        hashmap[i] = False
                    else:
                        hashmap[j] = False
            if hashmap[i]:
                return i
        return -1
