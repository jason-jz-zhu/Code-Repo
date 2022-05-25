"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# dfs
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        def dfs(n):
            if n in visited:
                return
            if n not in graph:
                graph[n] = Node(n.val)
            visited.add(n)
            for nxt in n.neighbors:
                if nxt not in graph:
                    graph[nxt] = Node(nxt.val)
                graph[n].neighbors.append(graph[nxt])
                dfs(nxt)
        
        
        graph = {}
        visited = set()
        dfs(node)
        return graph[node]

# dfs
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        graph = {}
        visited = set()
        stack = [node]
        
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            if n not in graph:
                graph[n] = Node(n.val)
            visited.add(n)
            for nxt in n.neighbors:
                if nxt not in graph:
                    graph[nxt] = Node(nxt.val)
                graph[n].neighbors.append(graph[nxt])
                stack.append(nxt)
        return graph[node]
            
# bfs
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        graph = {}
        visited = set()
        q = deque([node])
        
        while q:
            n = q.popleft()
            if n in visited:
                continue
            if n not in graph:
                graph[n] = Node(n.val)
            visited.add(n)
            for nxt in n.neighbors:
                if nxt not in graph:
                    graph[nxt] = Node(nxt.val)
                graph[n].neighbors.append(graph[nxt])
                q.append(nxt)
        return graph[node]
        
