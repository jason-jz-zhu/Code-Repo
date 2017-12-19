class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        if pid is None or len(pid) == 0:
            return []
        if ppid is None or len(ppid) == 0:
            return []
        if len(pid) != len(ppid):
            return []

        res = []
        queue = collections.deque([kill])
        hashmap = collections.defaultdict(list)
        for i in range(len(pid)):
            hashmap[ppid[i]].append(pid[i])

        while queue:
            curr = queue.popleft()
            res.append(curr)
            for node in hashmap[curr]:
                queue.append(node)

        return res

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        if pid is None or len(pid) == 0:
            return []
        if ppid is None or len(ppid) == 0:
            return []
        if len(pid) != len(ppid):
            return []

        res = []
        hashmap = collections.defaultdict(list)
        for i in range(len(pid)):
            hashmap[ppid[i]].append(pid[i])

        self.helper(kill, hashmap, res)
        return res

    def helper(self, kill, hashmap, res):
        res.append(kill)
        for node in hashmap[kill]:
            self.helper(node, hashmap, res)
