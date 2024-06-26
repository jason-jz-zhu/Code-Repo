
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sort_counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        return list(sort_counter.keys())[:k]

# use Counter as hash table and heapq
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Counter does the hash table function
        counter = collections.Counter(nums)
        # heap init
        heap = []
        # scan counter
        for key, cnt in counter.items():
            heapq.heappush(heap, (cnt, key))
            # max heap to k
            if len(heap) > k:
                heapq.heappop(heap)
        # extract the key
        return [x[-1] for x in heap]

# use bucket sort
class Solution(object):
    def topKFrequent(self, nums, k):
        # init bucket container
        bucket = [[] for _ in nums]
        # add num into bucket
        for num, freq in collections.Counter(nums).items():
            bucket[-freq].append(num)
        # get the top k
        return list(itertools.chain(*bucket))[:k]
