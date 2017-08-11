class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.hashmap[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.hashmap:
            target = value - key
            if target in self.hashmap and (key != target or self.hashmap[key] > 1):
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
