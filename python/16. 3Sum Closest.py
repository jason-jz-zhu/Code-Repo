class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) < 3:
            return None
        nums.sort()
        res = sys.maxint
        for i in xrange(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if (abs(s - target) < abs(res)):
                    res = s - target
                if s == target:
                    return target
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return target + res

        
