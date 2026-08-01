"""
LeetCode #658: Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order. An integer a is closer to x than an integer b if: |a - x| < |b - x|, or |a - x| == |b - x| and a < b.

Constraints:
1 <= k <= arr.length, 1 <= arr.length <= 10^5, 1 <= arr[i] <= 10^6
"""
class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr) - 1

        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l : r + 1]


solution = Solution()
print(solution.findClosestElements([2, 4, 5, 8], 2, 6))
print(solution.findClosestElements([2, 3, 4], 3, 1))
print(solution.findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(solution.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1))
