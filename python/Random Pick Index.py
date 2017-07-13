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

class Solution(object):

    def __init__(self, nums):
        self.nums = nums


    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])
