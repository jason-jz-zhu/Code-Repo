class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.dict = collections.defaultdict(set)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        self.dict[val].add(len(self.nums) - 1)
        return len(self.dict[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False

        index, last = self.dict[val].pop(), self.nums[-1]
        self.nums[index] = last
        if self.dict[last]:
            self.dict[last].add(index)
            self.dict[last].discard(len(self.nums) - 1)
        self.nums.pop()
        if not self.dict[val]:
            del self.dict[val]
        return True

    import random
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.nums)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
