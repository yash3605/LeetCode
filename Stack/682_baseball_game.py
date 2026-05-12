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
