
# Time:  O(n)
# Space: O(1)

class Solution:
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low, i = float("-inf"), -1
        for p in preorder:
            if p < low:
                return False
            while i >= 0 and p > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p
        return True

# Time:  O(n)
# Space: O(h)
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        low = -sys.maxint - 1
        stack = []
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True
