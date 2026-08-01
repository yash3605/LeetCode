"""
LeetCode #881: Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit. Return the minimum number of boats to carry every given person.

Constraints:
1 <= people.length <= 5 * 10^4, 1 <= people[i] <= limit <= 3 * 10^4
"""
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        res, l, r = 0, 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1

            if l <= r and remain >= people[l]:
                l += 1
        return res


solution = Solution()
print(solution.numRescueBoats([5,1,4,2], 6))
print(solution.numRescueBoats([1,3,2,3,2], 3))
print(solution.numRescueBoats([1, 2], 3))
print(solution.numRescueBoats([3,2,2,1], 3))
print(solution.numRescueBoats([3,5,3,4], 5))
