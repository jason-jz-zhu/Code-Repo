class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self._curr = 0
        self._numbers = range(maxNumbers)
        self._flag = [False] * maxNumbers


    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self._curr == len(self._numbers):
            return -1
        number = self._numbers[self._curr]
        self._curr += 1
        self._flag[number] = True
        return number

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return 0 <= number < len(self._numbers) and not self._flag[number]

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if not 0 <= number < len(self._numbers) or not self._flag[number]:
            return
        self._flag[number] = False
        self._curr -= 1
        self._numbers[self._curr] = number


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
