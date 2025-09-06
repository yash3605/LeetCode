from collections import defaultdict


class Solution:
    def majorityElementHM(self, nums: list[int]) -> list[int]:
        hs = {}
        n = len(nums)
        res = set()
        for i in range(n):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

            if hs[nums[i]] > n // 3:
                res.add(nums[i])
        return list(res)

    def majorityElement(self, nums: list[int]) -> list[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

            if len(count) >= 2:
                continue

            new_count = defaultdict(int)

            for num, c in count.items():
                new_count[num] = c - 1
            count = new_count

        res = []

        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([1]))
print(solution.majorityElement([1, 2]))
