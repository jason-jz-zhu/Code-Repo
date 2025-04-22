import heapq

heap = []

heapq.heappush(heap, (-3 , "a1"))
heapq.heappush(heap, (-4 , "a1"))
heapq.heappush(heap, (-2 , "a1"))


heapq.heappop(heap)

print(heap)