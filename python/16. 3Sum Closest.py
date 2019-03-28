class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        size = len(nums)
        res = float('inf')
        for i in range(size - 2):
            left, right = i + 1, size - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(res):
                    res = s - target
                if s == target:
                    return s
                elif s < target:
                    left += 1
                else:
                    right -= 1
        return res + target
