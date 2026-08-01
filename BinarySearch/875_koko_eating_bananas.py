"""
LeetCode #875: Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours. Koko can decide how many bananas to eat per hour (k). Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour. Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return. Return the minimum integer k such that she can eat all the bananas within h hours.

Constraints:
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""
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
