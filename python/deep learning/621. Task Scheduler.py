class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if tasks is None:
            return -1
        hashmap = collections.defaultdict(int)
        m = 0
        for task in tasks:
            hashmap[task] += 1
            m = max(m, hashmap[task])

        res = m + (m - 1) * n - 1
        for v in hashmap.values():
            if v == m:
                res += 1
        return max(res, len(tasks))
