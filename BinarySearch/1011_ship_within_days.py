"""
LeetCode #1011: Capacity To Ship Packages Within D Days

A conveyor belt has packages that must be shipped from one port to another within days days. The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship. Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Constraints:
1 <= days <= weights.length <= 5 * 10^4
1 <= weights[i] <= 500
"""
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res

solution = Solution()
print(solution.shipWithinDays([2,4,6,1,3,10], 4))
print(solution.shipWithinDays([1,2,3,4,5], 5))
print(solution.shipWithinDays([1,5,4,4,2,3], 3))
print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(solution.shipWithinDays([3,2,2,4,1,4], 3))
print(solution.shipWithinDays([1,2,3,1,1], 4))
