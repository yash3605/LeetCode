class Solution:
    def removeElements(self, nums: list[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1

        return j + 1
solution = Solution()
print(solution.removeElements([1,1,2,3,4], 1))
print(solution.removeElements([0,1,2,2,3,0,4,2], 2))
