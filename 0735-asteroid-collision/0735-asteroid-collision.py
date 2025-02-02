from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                val = stack.pop()
                if val > abs(asteroids[i]):  # If the last asteroid is larger, reinsert it and stop
                    stack.append(val)
                    break
                elif val == abs(asteroids[i]):  # If they are equal, both get destroyed
                    break
            else:
                stack.append(asteroids[i])  # Append if no collision occurs
                
        return stack