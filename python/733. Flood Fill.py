class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image is None or len(image) == 0:
            return None

        res = image
        if res[sr][sc] != newColor:
            self.bfs(res, sr, sc, newColor)
        return res

    def bfs(self, res, sr, sc, newColor):
        dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
        q = collections.deque([(sr, sc)])
        oldColor = res[sr][sc]
        res[sr][sc] = newColor
        while q:
            print(q)
            grid_x, grid_y = q.popleft()
            for k in range(4):
                x, y = grid_x + dx[k], grid_y + dy[k]
                if x < 0 or x >= len(res) or y < 0 or y >= len(res[0]):
                    continue
                if res[x][y] == oldColor:
                    res[x][y] = newColor
                    q.append((x, y))
