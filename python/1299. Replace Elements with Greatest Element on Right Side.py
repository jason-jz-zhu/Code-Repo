class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = float('-inf')
        for i in range(len(arr) - 1, -1, -1):
            tmp = max_num
            max_num = max(max_num, arr[i])
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                arr[i] = tmp
                
        return arr
