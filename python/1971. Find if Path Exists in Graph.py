# union find
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        ranks = [1 for _ in range(n)]
        def find(u):
            if u == parents[u]:
                return u
            parents[u] = find(parents[u])
            return parents[u]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
            elif ranks[pu] > ranks[pv]:
                parents[pv] = pu
            else:
                parents[pv] = pu
        
        for start, end in edges:
            union(start, end)
        
        ps = find(source)
        pd = find(destination)
        if ps == pd:
            return True
        return False
        
            
# dfs
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        visited = set()
        
        find = False
        def dfs(start, end):
            nonlocal find
            if start == end:
                find = True
                return True
            if find:
                return True
            
            visited.add(start)
            for nxt in graph[start]:
                if nxt in visited:
                    continue
                if dfs(nxt, end):
                    return True
            return False
        
        return dfs(source, destination)
        
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        visited = set()
        
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            
            for nxt in graph[node]:
                stack.append(nxt)
        return False
        
        
