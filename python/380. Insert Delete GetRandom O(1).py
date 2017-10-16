class RandomizedSet(object):
    import collections
    import random
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.hashmap = collections.defaultdict(int)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            return False
        self.nums.append(val)
        self.hashmap[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            return False
        idx, last = self.hashmap[val], self.nums[-1]
        self.nums[idx], self.hashmap[last] = last, idx
        self.nums.pop()
        del self.hashmap[val]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
