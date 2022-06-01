class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = -1
        for i, num in enumerate(nums):
            if max_num == num:
                ans = i
                continue 
            if num * 2 > max_num:
                return -1

        return ans
