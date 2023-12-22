class Solution:
    def maxScore(self, s: str) -> int:
        maxie = 0
        for i in range(len(s)-1):
            maxie = max(maxie, s[0:i+1].count('0')+s[i+1:].count('1'))
        return maxie
