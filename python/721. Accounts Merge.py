class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                email_to_name[email] = name


        visited = set()
        res = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                cache = []
                while stack:
                    node = stack.pop()
                    cache.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
                res.append([email_to_name[email]] + sorted(cache))
        return res
