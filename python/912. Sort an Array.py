// merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])
        return self.merge(l, r)
        
    def merge(self, left,  right):
        ans = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                ans.append(left[left_idx])
                left_idx += 1
            else:
                ans.append(right[right_idx])
                right_idx += 1
        ans += left[left_idx:]
        ans += right[right_idx:]
        return ans

    
    
// quick sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsort(nums, 0, len(nums) - 1)
        return nums
    
    def qsort(self, lst, low, high):
        if not lst or len(lst) == 1:
            return lst
        if low < high:
            p = self.partition(lst, low, high)
            self.qsort(lst, low, p - 1)
            self.qsort(lst, p + 1, high)
            
    def partition(self, lst, low, high):

        pivot = lst[high]
        i = low
        for j in range(low, high):
            if lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        
        lst[i], lst[high] = lst[high], lst[i]
        return i
