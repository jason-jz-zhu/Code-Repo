class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.ans = [[] for _ in range(self.size)]
        

    def add(self, key: int) -> None:
        tmp = self._eval_hash(key)
        if key not in self.ans[tmp]:
            self.ans[tmp].append(key)
        

    def remove(self, key: int) -> None:
        tmp = self._eval_hash(key)
        if key in self.ans[tmp]:
            self.ans[tmp].remove(key)

    def contains(self, key: int) -> bool:
        tmp = self._eval_hash(key)
        return key in self.ans[tmp]
        
    def _eval_hash(self, key):
        return key % self.size

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
