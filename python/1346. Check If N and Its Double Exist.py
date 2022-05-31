class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited = set()
        for item in arr:
            if 2 * item in visited or item / 2 in visited:
                return True
            visited.add(item)
        return False
