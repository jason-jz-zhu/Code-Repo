class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False
        visited = {i: False for i in xrange(n)}
        graph = {i: set([]) for i in xrange(n)}
        for item in edges:
            graph[item[0]].add(item[1])
            graph[item[1]].add(item[0])
        q = collections.deque([0])
        while q:
            head = q.popleft()
            if visited[head]:
                return False
            visited[head] = True
            for item in graph[head]:
                q.append(item)
                graph[item].remove(head)
        for i in visited:
            if not visited[i]:
                return False
        return True
