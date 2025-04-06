class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }


        for num in nums:
            curSum += num
           # print(curSum)
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
            #print(res)
            #print(prefixSums)

        return res
