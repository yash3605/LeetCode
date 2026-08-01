"""
LeetCode #853: Car Fleet

There are n cars going to the same destination along a one-lane road. The destination is target miles away. You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour). A car fleet is some non-empty set of cars driving at the same position and same speed. Return the number of car fleets that will arrive at the destination.

Constraints:
n == position.length == speed.length, 1 <= n <= 10^5, 0 <= position[i] <= target, 1 <= speed[i] <= 10^6
"""
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []
        for p, s in pair:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            

solution = Solution()
print(solution.carFleet(10, [1,4], [3,2]))
print(solution.carFleet(10, [4,1,0,7], [2,2,1,1]))
print(solution.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))
print(solution.carFleet(10,[3],[3]))
print(solution.carFleet(100, [0,2,4], [4,2,1]))
