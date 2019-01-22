class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        start, destination = tuple(start), tuple(destination)
        q = collections.deque([start])
        visited = set([])
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            if curr == destination:
                return True
            visited.add(curr)
            for neighbor in self.helper(maze, curr):
                q.append(neighbor)
        return False

    def helper(self, maze, node):
        res = []
        dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
        for k in range(4):
            curr_node = list(node)
            while curr_node[0] + dx[k] >= 0 and curr_node[0] + dx[k] < len(maze) and curr_node[1] + dy[k] >= 0 and curr_node[1] + dy[k] < len(maze[0]) and not maze[curr_node[0] + dx[k]][curr_node[1] + dy[k]]:
                curr_node[0] += dx[k]
                curr_node[1] += dy[k]
            res.append(tuple(curr_node))
        return res
