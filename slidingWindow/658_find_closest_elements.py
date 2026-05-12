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
