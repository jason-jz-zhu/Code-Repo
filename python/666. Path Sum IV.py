class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        self.res = 0
        hashmap = collections.defaultdict(int)
        for num in nums:
            key = num / 10
            val = num % 10
            hashmap[key] = val

        self.helper(nums[0]/10, 0, hashmap)

        return self.res

    def helper(self, root, pre_sum, hashmap):
        level, pos = root / 10, root % 10
        left = (level + 1) * 10 + pos * 2 - 1
        right = (level + 1) * 10 + pos * 2

        cur_sum = pre_sum + hashmap[root]

        if left not in hashmap and right not in hashmap:
            self.res += cur_sum
            return
        if left in hashmap:
            self.helper(left, cur_sum, hashmap)
        if right in hashmap:
            self.helper(right, cur_sum, hashmap)


class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        res = 0
        hashmap = collections.defaultdict(int)
        for num in nums:
            key = num / 10
            val = num % 10
            hashmap[key] = val

        q = collections.deque([nums[0] / 10])

        while q:
            node = q.popleft()
            level, pos = node / 10, node % 10
            left = (level + 1) * 10 + 2 * pos -1
            right = (level + 1) * 10 + 2 * pos
            if left not in hashmap and right not in hashmap:
                res += hashmap[node]

            if left in hashmap:
                hashmap[left] += hashmap[node]
                q.append(left)
            if right in hashmap:
                hashmap[right] += hashmap[node]
                q.append(right)

        return res
