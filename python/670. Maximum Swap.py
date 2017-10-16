# O(n3)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        lst = list(str(num))
        res = lst[:]
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                lst[i], lst[j] = lst[j], lst[i]
                if lst > res:
                    res = lst[:]
                lst[i], lst[j] = lst[j], lst[i]
        return int(''.join(res))

# O(n)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = map(int, str(num))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int(''.join(map(str, A)))
        return num
