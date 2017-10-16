class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        start = end = step = 0
        while end < len(nums) - 1:
            step += 1
            max_end = end
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:
                    return step
                max_end = max(max_end, i + nums[i])
            start, end = end + 1, max_end
        return step
