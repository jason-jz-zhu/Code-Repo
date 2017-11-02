class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        size = len(str(x)) - 1
        while x:
            left = x / (10 ** size)
            right = x % 10

            if left != right:
                return False

            x = (x % (10 ** size)) / 10
            size -= 2
        return True




class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        div = 1
        while x / div >= 10:
            div *= 10

        while x:
            left = x / div
            right = x % 10

            if left != right:
                return False

            x = (x % div) / 10
            div /= 100
        return True
