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
