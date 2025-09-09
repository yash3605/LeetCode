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
