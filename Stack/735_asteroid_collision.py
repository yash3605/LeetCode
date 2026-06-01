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
