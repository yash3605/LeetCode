class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        res = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

            res = mid

        if nums[res]< target:
            return res + 1
        else:
            return res


solution = Solution()
print(solution.searchInsert([-1,0,2,4,6,8], 5))
print(solution.searchInsert([-1,0,2,4,6,8], 10))
print(solution.searchInsert([1,3,5,6], 5))
print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))
print(solution.searchInsert([1,3,5,6], 0))
print(solution.searchInsert([1, 3, 5, 7, 9], 6))
