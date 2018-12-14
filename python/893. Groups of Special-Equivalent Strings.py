class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if A is None or len(A) == 0:
            return 0
        res = set()
        for a in A:
            odd = ''
            even = ''
            for i, c in enumerate(a):
                if i % 2 == 0 :
                    even += c
                else:
                    odd += c
            res.add(''.join(sorted(even) + sorted(odd)))
        return len(res)

class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if A is None or len(A) == 0:
            return 0

        return len(set([''.join(sorted(a[0::2]) + sorted(a[1::2])) for a in A]))
