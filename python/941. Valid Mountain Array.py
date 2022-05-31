class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        left, right, n = 0, len(arr) - 1, len(arr)
        while left + 1 < n and arr[left] < arr[left + 1]:
            left += 1
        while right - 1 >= 0 and arr[right - 1] > arr[right]:
            right -= 1
        return 0 < left == right < n - 1
        
