class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = collections.Counter(tasks)
        most = max(count.values())
        numMost = sum([1 for v in count.values() if v == most])
        res = (most - 1) * (n + 1) + numMost
        return max(res, len(tasks))


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        res = 0
        heap = []
        for c, f in collections.Counter(tasks).items():
            heapq.heappush(heap, (-f, c))

        while heap:
            i, tmp = 0, []
            while i <= n:
                res += 1
                if heap:
                    f, c = heapq.heappop(heap)
                    if f != -1:
                        tmp.append((f + 1, c))
                if not heap and not tmp:
                    break
                else:
                    i += 1
            for item in tmp:
                heapq.heappush(heap, item)
        return res

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        if tasks is None:
            return -1
        counter = collections.Counter(tasks)
        m = max(counter.values())

        res = m + (m - 1) * n - 1
        for val in counter.values():
            if val == m:
                res += 1
        return max(res, len(tasks))

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
