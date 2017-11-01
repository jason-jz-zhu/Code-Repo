class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        res, last = 0, -1
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        res = max(res, i - last)
                    else:
                        res = max(res, i - stack[-1])
        return res
                    
