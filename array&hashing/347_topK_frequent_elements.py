class Solution:
    def topKFrequentHM(self, nums: list[int], k: int) -> list[int]:
        hm = {}
        for num in nums:
            if num in  hm:
                hm[num] += 1
            else:
                hm[num] = 1

        arr: list[tuple[int, int]] = []
        for val, count in hm.items():
            arr.append((count, val))

        arr.sort(reverse=True)
        print(arr)
        return [arr[i][1] for i in range(k)]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
print(solution.topKFrequent([1], 1))
