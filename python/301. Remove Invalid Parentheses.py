# bfs
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        import collections
        if s is None or len(s) == 0:
            return ['']
        q = collections.deque([s])
        res, visited = [], set([])
        found = False
        while q:
            curr = q.popleft()
            if self.isValid(curr):
                found = True
                res.append(curr)
            elif not found:
                for i in range(len(curr)):
                    if curr[i] == '(' or curr[i] == ')':
                        tmp = curr[: i] + curr[i + 1:]
                        if tmp not in visited:
                            q.append(tmp)
                            visited.add(tmp)
        return res

    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0

class Solution(object):
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}
