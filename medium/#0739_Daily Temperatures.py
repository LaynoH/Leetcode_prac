class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)

        return answer

# ref: https://leetcode.com/problems/daily-temperatures/solutions/4653178/video-how-we-think-about-a-solution-python-javascript-java-c
