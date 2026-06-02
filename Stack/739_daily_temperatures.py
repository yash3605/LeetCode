class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res


solution = Solution()
print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(solution.dailyTemperatures([30,40,50,60]))
print(solution.dailyTemperatures([30,60,90]))
print(solution.dailyTemperatures([30,38,30,36,35,40,28]))
print(solution.dailyTemperatures([22,21,20]))
