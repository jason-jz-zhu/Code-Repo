class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points is None:
            return False

        hashmap = collections.defaultdict(set)
        min_x, max_x = float('inf'), float('-inf')

        for p in points:
            hashmap[p[0]].add(p[1])
            min_x = min(min_x, p[0])
            max_x = max(max_x, p[0])

        mid_x = (min_x + max_x) / 2.0
        for p in points:
            ref_x = 2 * mid_x - p[0]
            if ref_x not in hashmap or p[1] not in hashmap[ref_x]:
                return False
        return True
