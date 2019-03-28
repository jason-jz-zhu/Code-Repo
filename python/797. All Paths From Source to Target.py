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
