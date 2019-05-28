class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        steps = d = 0
        res = [[r0, c0]]
        while len(res) < R * C:
            if d in (0, 2):
                steps += 1
            for _ in range(steps):
                r0 += direction[d][0]
                c0 += direction[d][1]
                if r0 < 0 or r0 >= R or c0 < 0 or c0 >= C:
                    continue
                res.append([r0, c0])
            d = (d + 1) % 4
        return res
        
