class Logger:

    def __init__(self):
        self.hashmap = defaultdict(int)
        self.range = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashmap:
            self.hashmap[message] = timestamp + self.range
            return True
        if self.hashmap[message] <= timestamp:
            self.hashmap[message] = timestamp + self.range
            return True
        return False
