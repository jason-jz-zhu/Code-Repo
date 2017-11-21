class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path is None or len(path) == 0:
            return ''

        stack = []
        res = ''
        i = 0
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != '/':
                end += 1
            sub = path[i+1: end]
            if len(sub) > 0:
                if sub == '..':
                    if stack != []:
                        stack.pop()
                elif sub != '.':
                    stack.append(sub)
            i = end

        if stack == []:
            return '/'
        for s in stack:
            res += '/' + s
        return res
