# bfs 2025
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        q = collections.deque()
        for i in range(n):
            if len(graph[i]) == 1:
                q.append(i)

        nodeCount = n
        while nodeCount > 2:
            sz = len(q)
            nodeCount -= sz
            for _ in range(sz):
                cur = q.popleft()

                for neighbor in graph[cur]:
                    graph[neighbor].remove(cur)
                    if len(graph[neighbor]) == 1:
                        q.append(neighbor)
        return list(q)

# topological
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        degree = [0 for _ in range(n)]
        graph = {i: [] for i in range(n)}

        for i, j in edges:
            degree[i] += 1
            degree[j] += 1
            graph[i].append(j)
            graph[j].append(i)

        leaves = [i for i in range(n) if degree[i] == 1]
        nodes_number = n
        while nodes_number > 2:
            tmp = []
            for leave in leaves:
                degree[leave] = 0
                nodes_number -= 1
                for i in graph[leave]:
                    degree[i] -= 1
                    if degree[i] == 1:
                        tmp.append(i)
            leaves = tmp
        return leaves

    
# dfs TLE    
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            H = [dfs(nxt) for nxt in graph[node]]
            visited.remove(node)
            return max(H) + 1
        
        graph = defaultdict(list)
        
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        visited = set()
        ans = []
        min_H = float("inf")
        for i in range(n):
            H = dfs(i)
            if H < min_H:
                min_H = H
                ans = [i]
            elif H == min_H:
                ans.append(i)
        
        return ans
