class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= -(2**31) or n >= 2**31-1 or n == 0:
            return False
        
        while n/4 and abs(n)>1:
            n = n/4
        
        if n%4 == 0 or n==1:
            return True
        return False
