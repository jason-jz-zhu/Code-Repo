class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zero_cnt = arr.count(0)
        new_n = n + zero_cnt
        i = n - 1
        j = new_n - 1
        while j >= 0:
            if j < n:
                arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
            i -= 1
            

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                for j in reversed(range(i+1, len(arr)-1)):
                    arr[j+1] = arr[j]
                if i+1 < len(arr):
                    arr[i+1] = 0
                    i += 1
            i += 1
            
