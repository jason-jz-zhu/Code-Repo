class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if not A or len(A) == 0 or len(A[0]) == 0:
            return 0

        m, n = len(A), len(A[0])
        q = collections.deque([])
        has_find = False
        # visited = set()
        for i in range(m):
            if has_find:
                break
            for j in range(n):
                if A[i][j] == 1:
                    self.dfs(A, i, j, q)
                    has_find = True
                    break
        level = self.bfs(A, q)
        return level

    def dfs(self, A, i, j, q):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        if i < 0 or i >= len(A) or j < 0 or j >= len(A) or A[i][j] != 1:
            return
        A[i][j] = 2
        q.append((i, j))
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            self.dfs(A, x, y, q)

    def bfs(self, A, q):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        level = 0
        while q:
            q_size = len(q)
            for _ in range(q_size):
                curr_i, curr_j = q.popleft()
                for k in range(4):
                    x, y = curr_i + dx[k], curr_j + dy[k]
                    if x < 0 or x >= len(A) or y < 0 or y >= len(A[0]):
                        continue
                    if A[x][y] == 1:
                        return level
                    elif A[x][y] == 0:
                        A[x][y] = 2
                        q.append((x, y))
                    else:
                        continue

            level += 1
        return 0
        
