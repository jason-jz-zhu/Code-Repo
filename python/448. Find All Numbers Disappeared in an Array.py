class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        res = []
        m = len(nums)
        for num in nums:
            a = abs(num)
            if a == m:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])

        for i in range(1, m):
            if nums[i] > 0:
                res.append(i)
        if nums[0] > 0:
            res.append(m)
        return res
