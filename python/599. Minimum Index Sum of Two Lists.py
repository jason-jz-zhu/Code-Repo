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

        map = dict()
        res, index_sum = [], sys.maxint
        for i in xrange(len(list1)):
            map[list1[i]] = i
        for j in xrange(len(list2)):
            l1_index = map.get(list2[j])
            if l1_index is None:
                continue
            if l1_index + j < index_sum:
                res = [list2[j]]
                index_sum = l1_index + j
            elif l1_index + j == index_sum:
                res.append(list2[j])
        return res
                
