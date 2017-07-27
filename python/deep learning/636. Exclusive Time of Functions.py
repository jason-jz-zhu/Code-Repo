class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack, preTime = [], 0

        for log in logs:
            number, typ, time = log.split(':')
            number, time = int(number), int(time)
            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - preTime
                stack.append(number)
                preTime = time
            else:
                res[stack.pop()] += time - preTime + 1
                preTime = time + 1

        return res
