class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        boomTime = 0
        tmpTime = neededTime[0]
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                boomTime += min(tmpTime, neededTime[i+1])
                tmpTime = max(neededTime[i+1], tmpTime)
            else:
                tmpTime = neededTime[i+1]
        return boomTime

  # ref: https://www.youtube.com/watch?v=RIzny886yHM
