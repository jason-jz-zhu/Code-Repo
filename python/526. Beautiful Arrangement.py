
class Solution(object):
    def countArrangement(self, N):
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x})
                       for x in X
                       if x % i == 0 or i % x == 0)
        return count(N, set(range(1, N + 1)))

# TLE
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        Solution.res = 0
        visited = [False] * (N + 1)
        self.dfs(N, visited, 1)
        return Solution.res

    def dfs(self, N, visited, num):
        if num > N:
            Solution.res += 1
            return
        for i in range(1, N + 1):
            if not visited[i] and (i % num == 0 or num % i == 0):
                visited[i] = True
                self.dfs(N, visited, num + 1)
                visited[i] = False
