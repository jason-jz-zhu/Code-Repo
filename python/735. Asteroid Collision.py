class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if asteroids is None or len(asteroids) == 0:
            return []

        stack = []
        for node in asteroids:
            if node > 0:
                stack.append(node)
            else: # neg number
                while stack and stack[-1] > 0 and stack[-1] < abs(node):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(node)
                elif stack[-1] == abs(node):
                    stack.pop()
        return stack

                    
