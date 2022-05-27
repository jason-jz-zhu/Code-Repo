class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num*num for num in nums])


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0 for _ in range(len(nums))]
        l, r = 0, len(nums) - 1
        while l <= r:
            l_value, r_value = abs(nums[l]), abs(nums[r])
            if l_value > r_value:
                ans[r - l] = l_value * l_value
                l += 1
            else:
                ans[r - l] = r_value * r_value
                r -= 1
        return ans
