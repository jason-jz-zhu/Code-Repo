
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
                    
