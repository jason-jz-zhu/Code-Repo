
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if preorder is None or len(preorder) == 0:
            return True
        low = float('-inf')
        i = -1
        for node in preorder:
            if node < low:
                return False
            while i >= 0 and node > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = node
        return True

# Time:  O(n)
# Space: O(h)
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if preorder is None or len(preorder) == 0:
            return True
        low = float('-inf')
        stack = []
        for node in preorder:
            if node < low:
                return False
            while stack and node > stack[-1]:
                low = stack.pop()
            stack.append(node)
        return True
