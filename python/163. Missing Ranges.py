class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if nums is None:
            return []

        res = []
        prev = lower - 1
        nums.append(upper + 1)
        for num in nums:
            if num == prev + 2:
                res.append(str(num - 1))
            elif num > prev + 2:
                res.append(str(prev + 1) + '->' + str(num - 1))
            prev = num
        return res
