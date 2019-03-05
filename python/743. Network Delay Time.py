class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if not times or len(times) == 0 or len(times[0]) == 0:
            return 0

        self.graph = collections.defaultdict(list)
        for u, v, w in times:
            self.graph[u].append((w, v))

        self.dist = {node: float('inf') for node in range(1, N + 1)}

        self.dfs(K, 0)
        res = max(self.dist.values())
        return res if res < float('inf') else -1

    def dfs(self, node, elapsed):
        if elapsed >= self.dist[node]:
            return
        self.dist[node] = elapsed
        for time, nei in sorted(self.graph[node]):
            self.dfs(nei, elapsed + time)
