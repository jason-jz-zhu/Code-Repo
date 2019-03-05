class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = {}
        self.count = {}
        for i in range(1, n + 1):
            self.father[i] = i
            self.count[i] = 1

    def find(self, node):

        if self.father[node] == node:
            return node

        self.father[node] = self.find(self.father[node])

        return self.father[node]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count[root_b] += self.count[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.count[self.find(a)]
