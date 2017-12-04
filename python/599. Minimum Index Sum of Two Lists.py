class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        if list1 is None or len(list1) == 0:
            return []
        if list2 is None or len(list2) == 0:
            return []
        res = []
        idx_sum = float('inf')
        hashmap = collections.defaultdict(int)
        for i in range(len(list1)):
            hashmap[list1[i]] = i

        for j in range(len(list2)):
            tmp = list2[j]
            if tmp not in hashmap:
                continue
            if hashmap[tmp] + j < idx_sum:
                res = [tmp]
                idx_sum = hashmap[tmp] + j
            elif hashmap[tmp] + j == idx_sum:
                res.append(tmp)

        return res
