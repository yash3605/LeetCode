"""
LeetCode #735: Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row. For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed. Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Constraints:
2 <= asteroids.length <= 10^4, -1000 <= asteroids[i] <= 1000, asteroids[i] != 0.
"""
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []
        for a in asteroids:
            while res and a < 0 and res[-1] > 0:
                diff = a + res[-1]
                if diff < 0:
                    res.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    res.pop()
            if a:
                res.append(a)
        return res

solution = Solution()
print(solution.asteroidCollision([2,4,-4,-1]))
print(solution.asteroidCollision([5, 5]))
print(solution.asteroidCollision([7,-3,9]))
print(solution.asteroidCollision([5,10,-5]))
print(solution.asteroidCollision([8,-8]))
print(solution.asteroidCollision([10,2,-5]))
print(solution.asteroidCollision([3,5,-6,2,-1,4]))
