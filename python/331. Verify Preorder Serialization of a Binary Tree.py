class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for x in preorder.split(','):
            stack += [x]
            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != '#':
                stack = stack[: -3] + ['#']
        return len(stack) == 1 and stack[0] == '#'
        
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        diff = 1
        for node in nodes:
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2

        return diff == 0
