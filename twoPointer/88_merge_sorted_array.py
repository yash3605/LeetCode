"""
LeetCode #88: Merge Sorted Array

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order, and two integers m and n representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be stored inside the array nums1.

Constraints:
nums1.length == m + n, 0 <= m, n <= 200, 1 <= m + n <= 200, -10^9 <= nums1[i], nums2[i] <= 10^9
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        i, j, k = m - 1, n - 1, m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1


solution = Solution()
print(solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(solution.merge([1], 1, [], 0))
print(solution.merge([0], 0, [1], 1))
print(solution.merge([10, 20, 20, 40, 0, 0], 4, [1, 2], 2))
print(solution.merge([0, 0], 0, [1, 2], 2))
