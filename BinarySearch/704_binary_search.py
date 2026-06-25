class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1 
            else:
                hi = mid - 1
        return -1

solution = Solution()
print(solution.search([-1,0,2,4,6,8], 4))
print(solution.search([-1,0,2,4,6,8], 3))
print(solution.search([-1,0,3,5,9,12], 9))
print(solution.search([-1,0,3,5,9,12], 2))
