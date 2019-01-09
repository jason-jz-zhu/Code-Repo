class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        heap = []
        res = float('inf')
        rSum = 0
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            rSum += q
            if len(heap) == K:
                res = min(res, ratio * rSum)
            if len(heap) == K:
                rSum += heapq.heappop(heap)
        return res
