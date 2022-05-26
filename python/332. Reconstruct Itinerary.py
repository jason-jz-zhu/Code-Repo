# simi-DAG with loop, we need remove the graph element
# dfs
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for source, target in tickets:
            graph[source].append(target)
        
        for s, lst in graph.items():
            lst.sort()
        
        def dfs(start, path):
            nonlocal ans, find
            if len(path) == len(tickets) + 1:
                find = True
                ans = path
                return
            if find:
                return
            for i, nxt in enumerate(graph[start]):
                graph[start] = graph[start][:i] + graph[start][i+1:]
                dfs(nxt, path + [nxt])
                graph[start] = graph[start][:i] + [nxt] + graph[start][i:]
            
        
        ans = []
        find = False
        dfs("JFK", ["JFK"])
        return ans

#  Hierholzer's Algorithm (postorder DFS)
 class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for source, target in tickets:
            graph[source].append(target)
        
        for s, lst in graph.items():
            lst.sort(reverse=True)
        stack = ["JFK"]
        ans = []

        while len(stack) > 0:
            nxt = stack[-1]
            if nxt in graph and len(graph[nxt]) > 0:
                stack.append(graph[nxt].pop())
            else:
                ans.append(stack.pop())
        
        return ans[::-1]   
    
 
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
