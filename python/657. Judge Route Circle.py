class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves is None or len(moves) == 0:
            return True

        x = y = 0
        for move in moves:
            if move == 'R':
                x += 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'U':
                y -= 1
        if x == 0 and y == 0:
            return True
        return False
