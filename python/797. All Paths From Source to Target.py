# it is DAG, but need to find all path, no need visited, but need backtrack for path
# dfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(curr, path):
            if curr == len(graph) - 1:
                ans.append(path)
                return
            for nxt in graph[curr]:
                dfs(nxt, path + [nxt])
        
        ans = []
        dfs(0, [0])
        return ans

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.dfs(graph, 0, [0], res)
        return res

    def dfs(self, graph, curr, path, res):
        if curr == len(graph) - 1:
            res.append(path)
            return

        for node in graph[curr]:
            self.dfs(graph, node, path + [node], res)

# bfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []
        q = deque([[0]])
        while q:
            path = q.popleft()
            if path[-1] == len(graph) - 1:
                ans.append(path)
            else:
                q.extend([path + [child] for child in graph[path[-1]]])
        return ans
