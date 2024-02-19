class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev, curr = 0, 0, 1

        for i in range(n):
            prev2 = prev + curr
            prev, curr = curr, prev2
        return curr

# ref: https://leetcode.com/problems/climbing-stairs/solutions/4584184/beats-100-users-c-java-python-javascript-4-approaches-explained
