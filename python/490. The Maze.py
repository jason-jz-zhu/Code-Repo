class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        start, destination = tuple(start), tuple(destination)
        q = collections.deque([start])
        visited = set()
        while q:
            curr = q.popleft()
            if curr in visited:
                continue
            if curr == destination:
                return True
            visited.add(curr)
            for neighbor in self.neighbors(maze, curr):
                q.append(neighbor)
        return False

    def neighbors(self, maze, node):
        for dir in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                cur_node = list(node)
                while 0 <= cur_node[0]+dir[0] < len(maze) and \
                      0 <= cur_node[1]+dir[1] < len(maze[0]) and \
                      not maze[cur_node[0]+dir[0]][cur_node[1]+dir[1]]:
                    cur_node[0] += dir[0]
                    cur_node[1] += dir[1]
                yield tuple(cur_node)
