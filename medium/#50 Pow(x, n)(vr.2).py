class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        power = abs(n)
        times = 1
        
        while power:
            if power%2 == 1:
                times *= x
            
            power >>= 1
            x *= x
            
        if n > 0:
            return times
        else:
            return 1/times

# https://leetcode.com/problems/powx-n/discuss/2098772/O(Log-n)-Using-Binary-Exponentiation.-Easy-step-by-step-explanation.
