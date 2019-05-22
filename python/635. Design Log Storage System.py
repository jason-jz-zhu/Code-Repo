class LogSystem:

    def __init__(self):
        self._logs = []
        self._gra = {'Year': 4,
                  'Month': 7,
                  'Day': 10,
                  'Hour': 13,
                  'Minute': 16,
                  'Second': 19}

    def put(self, id: int, timestamp: str) -> None:
        self._logs.append((id, timestamp))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        idx = self._gra[gra]
        s, e = s[: idx], e[: idx]
        return [i for i, time in self._logs if s <= time[: idx] <= e]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
