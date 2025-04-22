from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        step = 0
        while q:
            step += 1
            sz = len(q)
            for _ in range(sz):
                point = q.popleft()
                for dir in dirs:
                    x, y = point[0] + dir[0], point[1] + dir[1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return step - 1 if step else 0  



# ---------2025--------
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        fresh_cnt = 0
        rotten = deque([])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes_passed = 0
        while rotten and fresh_cnt > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in dirs:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < rows and 0 <= yy < cols and grid[xx][yy] == 1:
                        fresh_cnt -= 1
                        grid[xx][yy] = 2
                        rotten.append((xx, yy))
        return minutes_passed if fresh_cnt == 0 else -1
                    
