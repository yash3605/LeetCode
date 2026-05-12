class Solution:
    def majorityElementHM(self, nums: list[int]) -> int:
        hs = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

            if hs[nums[i]] > n // 2:
                return nums[i]
        return 0

    def majorityElement(self, nums: list[int]) -> int:
        c = 0
        m = 0
        for num in nums:
            if c == 0:
                m = num
                c = 1
            elif m == num:
                c += 1

            else:
                c -= 1
        return m


solution = Solution()
print(solution.majorityElement([2,2,1,1,1,2,2]))
print(solution.majorityElement([3, 2, 3]))
