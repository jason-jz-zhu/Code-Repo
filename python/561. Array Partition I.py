class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        s = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            s += nums[i]
        return s




class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        cache = [0] * 20001
        max_value, min_value = 10000, -10000
        for num in nums:
            cache[num + max_value] += 1

        res = 0
        i = min_value
        first = True

        while i <= max_value:
            if cache[i + max_value] == 0:
                i += 1
                continue
            if first:
                res += i
                first= False
            else:
                first = True
            cache[i + max_value] -= 1
        return res

            
