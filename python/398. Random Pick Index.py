class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        nums = self.nums
        res = cnt = 0
        for i in xrange(len(nums)):
            if nums[i] == target:
                if random.randint(0, cnt) == 0:
                    res = i
                cnt += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
