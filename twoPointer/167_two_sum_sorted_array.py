"""
LeetCode #167: Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

Constraints:
2 <= numbers.length <= 3 * 10^4, -1000 <= numbers[i] <= 1000, numbers is sorted in non-decreasing order, -1000 <= target <= 1000
"""
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        le, ri = 0, len(numbers) - 1
        while le < ri:
            if (numbers[le] + numbers[ri]) == target:
                return [le + 1, ri + 1]
            elif (numbers[le] + numbers[ri]) > target:
                ri -= 1
            else:
                le += 1
        return []


solution = Solution()
print(solution.twoSum([1, 2, 3, 4], 3))
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([-1, 0], -1))
