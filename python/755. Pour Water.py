class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:

        if heights is None or len(heights) == 0:
            return []
        for _ in range(V):
            self.drop(heights, K)
        return heights


    def drop(self, h, K):
        best = K
        for d in (-1, 1):
            i = K + d
            while i >= 0 and i < len(h) and h[i] <= h[i - d]:
                if h[i] < h[best]:
                    best = i
                i += d
            if best != K:
                break
        h[best] += 1
