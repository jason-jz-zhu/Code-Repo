class Type:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.cnt == other.cnt and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        import heapq
        hashmap = collections.Counter(words)
        heap = []

        for word, cnt in hashmap.items():
            heapq.heappush(heap, (Type(cnt, word), word))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res[::-1]
