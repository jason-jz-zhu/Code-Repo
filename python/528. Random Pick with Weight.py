class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        _rs = w
        for i in range(1, len(w)):
            _rs[i] = _rs[i - 1] + w[i]
        self.rs = _rs

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randrange(0, self.rs[-1])
        start = 0
        end = len(self.rs) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.rs[mid] <= target:
                start = mid
            else:
                end = mid
        if target < self.rs[start]:
            return start
        return end


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
