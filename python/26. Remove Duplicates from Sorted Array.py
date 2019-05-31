class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = right = 0
        while right < len(nums):
            if right == 0 or nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
