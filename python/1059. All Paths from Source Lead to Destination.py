# dfs - basic way
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node):
            if node in visited:
                return False
            if len(graph[node]) == 0:
                return node == destination
            visited.append(node)
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            visited.remove(node)
            return True
        
        
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
        
        visited = []
        return dfs(source)
      
# dfs - adv way
# visited[i] == 0 means not visited before,
# visited[i] == 1 means visited in the current path,
# visited[i] == 2 means visited before.
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            if len(graph[node]) == 0:
                return node == destination
            visited[node] = 1
            for nxt in graph[node]:
                if not dfs(nxt):
                    return False
            visited[node] = 2
            return True
        
        
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
        
        visited = [0 for _ in range(n)]
        return dfs(source)
