class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def helper(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                else:
                    stack = stack[:-1]
            return stack

        return helper(S) == helper(T)


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        si, ti = len(S) - 1, len(T) - 1
        cs = ct = 0
        while si >= 0 or ti >= 0:
            while si >= 0:
                if S[si] == '#':
                    cs += 1
                    si -= 1
                elif S[si] != '#' and cs > 0:
                    cs -= 1
                    si -= 1
                else:
                    break

            while ti >= 0:
                if T[ti] == '#':
                    ct += 1
                    ti -= 1
                elif T[ti] != '#' and ct > 0:
                    ct -= 1
                    ti -= 1
                else:
                    break

            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                return False
            if (ti >= 0 and si >= 0) and S[si] != T[ti]:
                return False
            si -= 1
            ti -= 1
        return True
