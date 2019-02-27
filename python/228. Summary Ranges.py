class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums or len(nums) == 0:
            return []

        res = []
        m = len(nums)
        end = 0
        while end < m:
            start = end
            while end < m - 1 and nums[end] + 1 == nums[end + 1]:
                end += 1
            if nums[start] != nums[end]:
                res.append(str(nums[start]) + '->' + str(nums[end]))
            else:
                res.append(str(nums[start]))
            end += 1
        return res
