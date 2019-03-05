class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.count = n
        self.father = {i: i for i in range(1, n + 1)}

    def find(self, node):
        if node == self.father[node]:
            return node

        self.father[node] = self.find(self.father[node])

        return self.father[node]

    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.count
