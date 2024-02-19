class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 1, 2
        i = 1
        while i < n:
            step1, step2 = step2, step1+step2
            i += 1
        return step1

# ref: https://leetcode.com/problems/climbing-stairs/solutions/4584184/beats-100-users-c-java-python-javascript-4-approaches-explained/comments/2215625
