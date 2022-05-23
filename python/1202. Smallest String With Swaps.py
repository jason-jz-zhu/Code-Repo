# union find 
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parents = [i for i in range(len(s))]
        ranks = [1 for _ in range(len(s))]
        cnt = len(s)
        
        def find(u):
            if parents[u] == u:
                return u
            parents[u] = find(parents[u])
            return parents[u]
        
        def union(u, v):
            nonlocal cnt
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
            elif ranks[pu] > ranks[pv]:
                parents[pv] = pu
            else:
                parents[pv] = pu
                ranks[pu] += 1
            cnt -= 1
            return True
        
        ans = []
        tmp = defaultdict(list)
        for x, y in pairs:
            union(x, y)
        print(parents)
        for i in range(len(parents)):
            tmp[find(i)].append(s[i])
            
        for key in tmp.keys():
            tmp[key].sort(reverse=True)
        
        for i in range(len(s)):
            ans.append(tmp[find(i)].pop())
        
        return ''.join(ans)
      
# dfs
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True
            tmp.append(i)
            for j in graph[i]:
                dfs(j)
            
        graph = defaultdict(list)
        for start, end in pairs:
            graph[start].append(end)
            graph[end].append(start)
        visited = [False for _ in range(len(s))]
        ans = list(s)
        for i in range(len(s)):
            if not visited[i]:
                tmp = []
                dfs(i)
                tmp.sort()
                chars = [ans[k] for k in tmp]
                chars.sort()
                for i in range(len(tmp)):
                    ans[tmp[i]] = chars[i]
        return ''.join(ans)
                
        
 
