import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = i
            for j in range(1, int(math.sqrt(i))+1):
                dp[i] = min(dp[i], dp[i-(j**2)]+1)
        return dp[-1]

# ref: https://leetcode.com/problems/perfect-squares/solutions/4696690/5-lines-of-code-dp-fully-explained-with-example-easy-to-understand-beat-94-users/
