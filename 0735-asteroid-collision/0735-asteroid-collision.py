class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: list[int] = []

        for a in asteroids:
            alive = True
            # Only collide when current moves left (-) and top moves right (+)
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()      # top asteroid destroyed, keep checking
                elif stack[-1] == -a:
                    stack.pop()      # both destroyed
                    alive = False
                else:
                    alive = False    # top asteroid survives, current destroyed

            if alive:
                stack.append(a)

        return stack