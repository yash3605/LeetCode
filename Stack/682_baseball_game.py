"""
LeetCode #682: Baseball Game

You are keeping the scores for a baseball game with strange rules. Given a list of strings operations, return the sum of the points on the record. The operations are: Integer x (record a new score of x), "+" (record a new score that is the sum of the previous two scores), "D" (record a new score that is the double of the previous score), "C" (invalidate the previous score, removing it from the record).

Constraints:
1 <= operations.length <= 1000, operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
"""
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        score = []
        top = -1

        for ops in operations:
            if ops == "+":
                score.append(score[top] + score[top - 1])
                top += 1
            elif ops == "C":
                score.pop()
                top -= 1
            elif ops == "D":
                score.append(score[top] * 2)
                top += 1
            else:
                score.append(int(ops))
                top += 1

        totalScore = 0
        for num in score:
            totalScore += num 

        return totalScore

        

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))
print(solution.calPoints(["5","-2","4","C","D","9","+","+"]))
print(solution.calPoints(["1","C"]))
print(solution.calPoints(["1","2","+","C","5","D"]))
print(solution.calPoints(["5","D","+","C"]))
