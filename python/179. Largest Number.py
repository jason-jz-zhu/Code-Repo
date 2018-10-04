class Larger(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums is None or len(nums) == 0:
            return ''

        nums = [str(num) for num in nums]
        nums.sort(key=Larger)
        largest = ''.join(nums)
        return '0' if largest[0] == '0' else largest
