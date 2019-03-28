class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)
        for i in range(size):
            if type(nums[i]) != int:
                continue
            if nums[i] % size == 0:
                continue

            direction = (nums[i] > 0)
            mark = str(i)
            while type(nums[i]) == int and nums[i] % size != 0 and direction ^ (nums[i] < 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % size
                if nums[i] == mark:
                    return True
        return False
                
