class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        length = len(nums)
        ans = [0] * (2*length)

        for i in range(length):
            ans[i] = nums[i]
            ans[i+length] = nums[i]

        return ans
