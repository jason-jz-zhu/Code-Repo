class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = collections.Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]




class Type:
    def __init__(self, cnt, w):
        self.cnt = cnt
        self.w = w

    def __lt__(self, other):
        if self.cnt == other.cnt:
            return self.w.lower() > other.w.lower()
        return self.cnt < other.cnt

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = []
        for w, cnt in counter.items():
            heapq.heappush(heap, Type(cnt, w))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).w)
        return res[::-1]
