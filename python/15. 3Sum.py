
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values
                continue
            target = - nums[i]
            start = i + 1
            pairs = self.twoSumTarget(nums, start, target)
            for pair in pairs:
                pair.append(nums[i])
                res.append(pair)

        return res

    def twoSumTarget(self, nums, start, target):
        lo, hi = start, len(nums) - 1
        res = []
        while lo < hi:
            s = nums[lo] + nums[hi]
            left, right = nums[lo], nums[hi]
            if s < target:
                while lo < hi and nums[lo] == left:
                    lo += 1
            elif s > target:
                while lo < hi and nums[hi] == right:
                    hi -= 1
            else:
                res.append([left, right])
                while lo < hi and nums[lo] == left:
                    lo += 1
                while lo < hi and nums[hi] == right:
                    hi -= 1
        return res


# ------------2025------------
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                s = nums[start] + nums[end]
                if s == target:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif s < target:
                    start += 1
                else:
                    end -= 1
        return res
