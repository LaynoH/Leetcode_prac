class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flips, flag = 0, 0

        for i in s:
            if i == '1':
                flag +=1
            elif flag:
                flag -= 1
                flips += 1
        return flips

# ref: https://leetcode.com/problems/flip-string-to-monotone-increasing/solutions/3061225/python-3-7-lines-w-explanation-and-example-t-m-100-96/
