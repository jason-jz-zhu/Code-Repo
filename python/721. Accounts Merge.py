# dfs
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = collections.defaultdict(set)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_to_name[email] = name

        visited = set()
        res = []
        for email in graph:
            if email not in visited:
                path = set()
                self.get_all_emails(email, graph, visited, path)
                res.append([email_to_name[email]] + sorted(path))
        return res

    def get_all_emails(self, email, graph, visited, path):
        path.add(email)
        visited.add(email)
        for neighbor in graph[email]:
            if neighbor in visited:
                continue
            self.get_all_emails(neighbor, graph, visited, path)

# union find
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.father = collections.defaultdict()
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in self.father:
                    self.father[email] = email
                    email_to_name[email] = name
                self.union(account[1], email)

        res = collections.defaultdict(list)

        for email in self.father:
            root_email = self.find(email)
            res[root_email].append(email)
        return [[email_to_name[root_email]] + sorted(emails) for root_email, emails in res.items()]

    def find(self, email):
        if email == self.father[email]:
            return email
        self.father[email] = self.find(self.father[email])
        return self.father[email]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
