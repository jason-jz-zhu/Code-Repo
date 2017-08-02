class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 4:
            return []
        res = []
        nums.sort()
        l = len(nums)
        for i in xrange(l - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, l - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                s = target - nums[i]- nums[j]
                left, right = j + 1, l - 1
                while left < right:
                    if nums[left] + nums[right] == s:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > s:
                        right -= 1
                    else:
                        left += 1
        return res
