# dfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if isConnected is None or len(isConnected) == 0:
            return 0
        if isConnected[0] is None or len(isConnected[0]) == 0:
            return 0
        
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)
        
        ans = 0
        visited = [False for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                ans += 1
        return ans
                

# bfs
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if M is None or len(M) == 0:
            return 0
        if M[0] is None or len(M[0]) == 0:
            return 0

        res = 0
        visited = [False for _ in range(len(M))]
        for i in range(len(M)):
            if not visited[i]:
                self.bfs(M, i, visited)
                res += 1
        return res

    def bfs(self, M, i, visited):
        q = collections.deque([i])
        visited[i] = True
        while q:
            t = q.popleft()
            for j in range(len(M)):
                if M[t][j] == 1 and not visited[j]:
                    q.append(j)
                    visited[j] = True

# union find
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        ranks = [1 for _ in range(len(isConnected))]
        
        def find(u):
            while u != parents[u]:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
            elif ranks[pu] > ranks[pv]:
                parents[pv] = pu
            else:
                parents[pu] = pv
                ranks[pu] += 1
            return True
        
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        ans = set()
        for i in range(len(isConnected)):
            ans.add(find(i))
        return len(ans)
                    
