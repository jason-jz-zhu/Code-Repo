class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''

        counter = collections.Counter(s)
        res = ''
        counter_sort = sorted(counter.items(), key = lambda (k, v): (v, k))
        for key, cnt in counter_sort:
            res += key * cnt
        return res[::-1]
            

# using hash and heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""

        hash = {}
        for ele in s:
            hash[ele] = hash.get(ele, 0) + 1

        import heapq
        heap = []
        for key, time in hash.iteritems():
            heapq.heappush(heap, (time, key))

        res = ''
        while heap:
            time, key = heapq.heappop(heap)
            res += time * key
        return res[::-1]

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join([char * time for char, time in collections.Counter(s).most_common()])
