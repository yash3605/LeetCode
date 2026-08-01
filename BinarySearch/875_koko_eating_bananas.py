import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r)//2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
        

solution = Solution()
print(solution.minEatingSpeed([1,4,3,2], 9))
print(solution.minEatingSpeed([25,10,23,4], 4))
print(solution.minEatingSpeed([3,6,7,11], 8))
print(solution.minEatingSpeed([30,11,23,4,20], 5))
print(solution.minEatingSpeed([30,11,23,4,20], 6))
