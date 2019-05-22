class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if tickets is None or len(tickets) == 0:
            return []

        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for frm, tos in graph.items():
            tos.sort(reverse=True)

        res = []
        self.dfs(graph, 'JFK', res)
        return res[::-1]

    def dfs(self, graph, source, res):
        while graph[source]:
            v = graph[source].pop()
            self.dfs(graph, v, res)
        res.append(source)
