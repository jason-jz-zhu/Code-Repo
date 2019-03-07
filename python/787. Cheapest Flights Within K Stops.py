# bfs
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        graph = collections.defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))

        q = collections.deque([(src, 0)])
        res = float('inf')
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr_node, curr_cost = q.popleft()
                if curr_node == dst:
                    res = min(res, curr_cost)
                for neighbor, neighbor_cost in graph[curr_node]:
                    if curr_cost + neighbor_cost > res:
                        continue
                    q.append((neighbor, curr_cost + neighbor_cost))
            if step > K:
                break
            step += 1
        return res if res != float('inf') else -1

# dfs
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end, price))
        self.res = float('inf')
        visited = set([src])
        self.dfs(src, dst, K + 1, 0, visited, graph)
        return self.res if self.res != float('inf') else -1

    def dfs(self, src, dst, k, cost, visited, graph):
        if src == dst:
            self.res = cost
            return
        if k == 0:
            return
        for neighbor, neighbor_cost in graph[src]:
            if neighbor in visited:
                continue
            if cost + neighbor_cost > self.res:
                continue
            visited.add(neighbor)
            self.dfs(neighbor, dst, k - 1, cost + neighbor_cost, visited, graph)
            visited.remove(neighbor)

# Bellman-Ford
# space  o(n2)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [[float('inf') for _ in range(n)] for _ in range(K + 2)]
        dp[0][src] = 0
        for i in range(1, K + 2):
            dp[i][src] = 0
            for start, end, price in flights:
                dp[i][end] = min(dp[i][end], dp[i - 1][start] + price)

        return dp[K + 1][dst] if dp[K + 1][dst] != float('inf') else -1

# space o(n)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [float('inf') for _ in range(n)]
        dp[src] = 0
        for i in range(1, K + 2):
            tmp = dp[:]
            for start, end, price in flights:
                tmp[end] = min(tmp[end], dp[start] + price)
            dp = tmp
        return dp[dst] if dp[dst] != float('inf') else -1

# Dijkstra's
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)

        for start, end, price in flights:
            graph[start][end] = price

        heap = [(0, src, K + 1)]
        while heap:
            price, start, k = heapq.heappop(heap)
            if start == dst:
                return price
            if k > 0:
                for end in graph[start]:
                    heapq.heappush(heap, (price + graph[start][end], end, k - 1))

        return -1
