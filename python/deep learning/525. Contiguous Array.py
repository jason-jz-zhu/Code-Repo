class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        res = s = 0
        hashmap = {0: -1}
        for i, v in enumerate(nums):
            s += -1 if v == 0 else 1
            if s in hashmap:
                res = max(res, i - hashmap[s])
            else:
                hashmap[s] = i
        return res

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {0 : -1}
        res, sum = 0, 0
        for i, n in enumerate(nums):
            sum += 2 * n - 1
            if sum in map:
                res = max(res, i - map[sum])
            else:
                # record the oldest sum's index
                map[sum] = i
        return res


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [0] * len(nums)
        map = collections.defaultdict(int)
        sum = 0
        res = 0
        for i, n in enumerate(nums):
            sum += 2 * n - 1
            sums[i] = sum
            # record the latest sum's index
            map[sum] = max(map[sum], i)

        for i, m in enumerate(sums):
            if m == 0:
                res = max(res, i + 1)
            else:
                res = max(res, map[m] - i)
        return res
