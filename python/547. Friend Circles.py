# dfs
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
                self.dfs(M, i, visited)
                res += 1
        return res

    def dfs(self, M, i, visited):
        visited[i] = True
        for j in range(len(M)):
            if M[i][j] == 1 and not visited[j]:
                self.dfs(M, j, visited)

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
        while q:
            t = q.popleft()
            visited[t] = True
            for j in range(len(M)):
                if M[t][j] == 1 and not visited[j]:
                    q.append(j)
