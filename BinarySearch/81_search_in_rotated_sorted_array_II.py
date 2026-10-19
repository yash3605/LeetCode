class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m  + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False
        
solution = Solution()
print(solution.search([3,4,4,5,6,1,2,2], 1))
print(solution.search([3,5,6,0,0,1,2], 4))
print(solution.search([2,5,6,0,0,1,2], 0))
print(solution.search([2,5,6,0,0,1,2], 3))
