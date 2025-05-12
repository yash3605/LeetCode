'''class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []

        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]

        return len(tmp)
'''
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
