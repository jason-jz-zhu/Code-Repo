class LogSystem(object):

    def __init__(self):
        self._logs = []
        self._hashmap = {'Year': 4, 'Month': 7, 'Day': 10, \
                        'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self._logs.append((id, timestamp))


    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        i = self._hashmap[gra]
        start = s[: i]
        end = e[: i]
        return [id for id, timestamp in self._logs if start <= timestamp[: i] <= end]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
