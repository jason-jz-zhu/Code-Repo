"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        self.graph = {}
        self.visit = set()
        self._helper(node)
        return self.graph[node]
        
    def _helper(self, n):
        if n in self.visit:
            return
        if n not in self.graph:
            self.graph[n] = Node(n.val)
        self.visit.add(n)
        for nxt in n.neighbors:
            if nxt not in self.graph:
                self.graph[nxt] = Node(nxt.val)
            self.graph[n].neighbors.append(self.graph[nxt])
            self._helper(nxt)
            

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
        
