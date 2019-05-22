class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._hashmap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._hashmap:
            return ''

        arr = self._hashmap[key]
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] > timestamp:
                end = mid
            else:
                start = mid
        if arr[end][1] <= timestamp:
            return arr[end][0]
        elif arr[start][1] <= timestamp < arr[end][1]:
            return arr[start][0]
        else:
            return ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
