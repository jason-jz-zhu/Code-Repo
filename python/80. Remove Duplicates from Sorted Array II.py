class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        left = right = 0
        while right < len(nums):
            if right < 2 or nums[left - 2] != nums[right] or nums[left - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
        
